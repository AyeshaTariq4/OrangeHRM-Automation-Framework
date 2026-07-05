# OrangeHRM Automation Framework

## Project Description

This project is a Selenium Automation Framework developed using Python and the Page Object Model (POM) design pattern. It automates important OrangeHRM functionalities including Login, Dashboard Verification, Admin User Search, Employee Creation, and Logout.

The project is designed with a clean folder structure, reusable code, and separate page classes to make automation easy to maintain and extend.

---

## Features

- Login Automation
- Dashboard Verification
- Admin User Search
- Add New Employee (PIM)
- Logout Automation
- Page Object Model (POM)
- Reusable Code Structure
- WebDriver Manager Integration

---

## Technologies Used

- Python
- Selenium WebDriver
- WebDriver Manager
- ChromeDriver
- VS Code
- Git & GitHub

---

## Project Structure

```
OrangeHRM-Automation-Framework/
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── admin_page.py
│   ├── pim_page.py
│   └── logout_page.py
│
├── tests/
│   └── test_login.py
│
├── screenshots/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/AyeshaTariq4/OrangeHRM-Automation-Framework.git
```

Install dependencies

```
pip install -r requirements.txt
```

Run the project

```
python -m tests.test_login
```

---

## Automated Workflow

- Login
- Verify Dashboard
- Search User in Admin Module
- Add Employee from PIM Module
- Logout

---

## Screenshots

Screenshots are available inside the **screenshots** folder.

---

## Future Improvements

- Pytest Integration
- HTML Reports
- Data Driven Testing
- Cross Browser Testing
- Jenkins CI/CD Integration

---

## Author

**Ayesha Tariq**

DevOps & Cloud Engineer

Python | Selenium | AWS | Azure | Docker | Kubernetes