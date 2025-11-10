University Hostel Management System – Project Overview:

The University Hostel Management System is a full-stack web application designed to streamline hostel operations such as student registration, room allocation, staff management, and payment tracking.
This system replaces traditional manual record-keeping with a centralized and digital approach using Flask, HTML, CSS, JavaScript, and MySQL.

It demonstrates the integration of backend logic, frontend interface, and database management — offering an efficient, user-friendly, and scalable hostel administration tool.

2.Project Features:
🧑‍🎓 Student Management: Register, update, and manage student details.
🏠 Room Allocation: Assign and manage rooms efficiently with vacancy tracking.
👩‍💼 Staff Management: Maintain records of hostel staff and their roles.
💳 Payment Tracking: Record and view student payments and due balances.
📊 Dashboard Overview: Admin panel with summary of all hostel operations.
🔐 Authentication System: Secure login for administrators.
💾 Database Integration: All records are stored in a structured MySQL database.

3.Technologies Used:

->Frontend: HTML5, CSS3, JavaScript, Jinja2 Templates
->Backend: Python Flask Framework
->Database: MySQL (via SQLAlchemy ORM)
->Tools / IDEs: MySQL Workbench, Visual Studio Code
->Version Control: Git & 

4.Setup Instructions:
Prerequisites
   Python 3.8 or higher
   pip (Python package manager)
   MySQL Server and MySQL Workbench
   Web browser

A.Clone the Repository:
git clone https://github.com/vaishnavi-aluvoju/University-Hostel-Management-System.git
cd University-Hostel-Management-System

B.Install Dependencies:
pip install -r requirements.txt

C.Setup the Database:
  Open MySQL Workbench and run:
    CREATE DATABASE hostel_db;
    USE hostel_db;

Then execute:
ddl_statements.sql – to create all tables
dml_statements.sql – to insert sample data

D.Run the Application:
python app.py

Open browser → http://localhost:127.0.0.1:5000

E.Testing & Validation:

✅ MySQL Workbench: Verified student, room, payment, and staff records.

✅ Frontend: Ensured smooth navigation between pages.

✅ Admin Panel: Tested CRUD operations (Add, Edit, Delete, View).

✅ Data Consistency: Validated relationships through joins and constraints.

F.Troubleshooting:

  1.Error: “Access denied for user 'root'@'localhost'”
  Solution: Update username/password in app.py.

  2.Error: “Module not found: flask_sqlalchemy”
  Solution: Run pip install flask flask_sqlalchemy.

  3.Error: “Port already in use”
  Solution: Stop previous Flask instance or change port in app.py.

  Repository Link

G.GitHub Repository:
https://github.com/vaishnavi-aluvoju/University-Hostel-Management-System

👩‍💻 Author
Vaishnavi Aluvoju

