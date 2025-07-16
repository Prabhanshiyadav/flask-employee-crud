# 👩‍💼 Flask Employee Management System

A full-featured **CRUD web application** built with **Flask** and **Tailwind CSS** to manage employee data. Includes smart filtering, search, salary insights, and an admin dashboard.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-lightgrey)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-Styling-blueviolet)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🚀 Features

- 🔍 **Search & Filter** by name, department, or salary range
- 🧑‍💼 **Add / Edit / Delete Employees**
- 📊 **Admin Dashboard** with:
  - Total Employees
  - Average, Min & Max Salary
  - Employees by Department
  - Recently Added Employees
- ✅ **Confirmation Modal** for deletions
- 🌈 **Modern UI** with Tailwind CSS
- 💾 **SQLite database** with SQLAlchemy ORM

---

## 📸 Screenshots

| Home Page | Admin Dashboard |
|-----------|-----------------|
| ![home](assets/home.png) | ![dashboard](assets/dashboard.png) |

---

## ⚙️ Tech Stack

| Technology | Usage |
|------------|--------|
| Python | Core Programming Language |
| Flask | Web Framework |
| Jinja2 | Templating Engine |
| SQLAlchemy | ORM for database |
| SQLite | Lightweight DB |
| Tailwind CSS | Modern styling |
| Chart.js | Visualizations in dashboard |

---



📂 Folder Structure

employee_app/
│
├── app.py                 # Main Flask app
├── models.py              # SQLAlchemy models
├── templates/             # All Jinja2 HTML templates
│   ├── base.html
│   ├── home.html
│   ├── create.html
│   ├── edit.html
│   ├── listemp.html
│   └── dashboard.html
├── static/                # Tailwind (if customized locally)
├── requirements.txt       # Python dependencies
├── README.md              # You're here
└── employees.db           # SQLite database (auto-generated)



## 🛠️ Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/Prabhanshiyadav/flask-employee-crud.git
cd flask-employee-crud


2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Run the App
python app.py