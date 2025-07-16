from flask import Flask, render_template, request, redirect, url_for
from models import db, Employee
from config import Config
from sqlalchemy import func

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        dept = request.form['department']
        salary = float(request.form['salary'])

        new_emp = Employee(name=name, department=dept, salary=salary)
        db.session.add(new_emp)
        db.session.commit()
        return redirect(url_for('listemp'))

    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    emp = Employee.query.get_or_404(id)
    if request.method == 'POST':
        emp.name = request.form['name']
        emp.department = request.form['department']
        emp.salary = float(request.form['salary'])

        db.session.commit()
        return redirect(url_for('listemp'))
    return render_template('edit.html', emp=emp)

@app.route('/delete/<int:id>')
def delete(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('listemp'))

@app.route('/listemp')
def listemp():
    query = Employee.query

    search = request.args.get('search')
    if search:
        query = query.filter(
            (Employee.name.ilike(f'%{search}%')) |
            (Employee.department.ilike(f'%{search}%'))
        )

    dept = request.args.get('department')
    if dept and dept != "All":
        query = query.filter(Employee.department == dept)

    min_salary = request.args.get('min_salary')
    max_salary = request.args.get('max_salary')
    if min_salary:
        query = query.filter(Employee.salary >= float(min_salary))
    if max_salary:
        query = query.filter(Employee.salary <= float(max_salary))

    employees = query.all()
    departments = [d[0] for d in db.session.query(Employee.department).distinct()]
    return render_template('listemp.html', employees=employees, departments=departments)

@app.route('/admin/dashboard')
def admin_dashboard():
    total_employees = Employee.query.count()
    avg_salary = db.session.query(func.avg(Employee.salary)).scalar()
    max_salary = db.session.query(func.max(Employee.salary)).scalar()
    min_salary = db.session.query(func.min(Employee.salary)).scalar()

    dept_counts = db.session.query(Employee.department, func.count(Employee.id)) \
                            .group_by(Employee.department).all()

    recent_employees = Employee.query.order_by(Employee.id.desc()).limit(5).all()

    return render_template('dashboard.html',
                           total=total_employees,
                           avg=round(avg_salary or 0, 2),
                           max_salary=max_salary,
                           min_salary=min_salary,
                           dept_counts=dept_counts,
                           recent_employees=recent_employees)



if __name__ == "__main__":
    app.run()
