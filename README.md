University Hostel Management System
📖 Project Overview

The University Hostel Management System is a full-stack web-based application built using Flask (Python) and MySQL.
It helps in efficiently managing hostel operations such as student registration, room allocation, staff management, and payment tracking through a centralized system.
This project demonstrates real-world database management and full-stack development integration with an interactive dashboard for administrators.

🚀 Features

🧑‍🎓 Student Management – Add, update, and view student records

🏠 Room Allocation – Assign rooms based on availability

👩‍💼 Staff Management – Manage staff records and roles

💳 Payment Tracking – Maintain student payment details

📊 Admin Dashboard – Monitor hostel data and analytics

🔐 Authentication System – Secure admin login

💾 Database Integration – Uses MySQL for structured data storage

🧰 Technologies Used
Category	        Technologies
Frontend	        HTML5, CSS3, JavaScript, Jinja2 Templates
Backend	            Python Flask Framework
Database	        MySQL (via SQLAlchemy ORM)
Tools & Platforms	MySQL Workbench, Visual Studio Code, Git, GitHub
⚙️ Installation and Setup Instructions
Prerequisites

1.Make sure you have:

2.Python 3.8 or higher

3.pip (Python package manager)

4.MySQL Server

5.MySQL Workbench

6.Modern web browser

Setup Steps:
1️⃣ Clone the Repository
git clone https://github.com/vaishnavi-aluvoju/University-Hostel-Management-System.git
cd University-Hostel-Management-System

2️⃣ Install Required Dependencies:
pip install -r requirements.txt

3️⃣ Create and Configure Database:

Open MySQL Workbench and run:

CREATE DATABASE hostel_db;
USE hostel_db;


Then execute your DDL (table creation) and DML (sample data) scripts.

4️⃣ Update Database Connection (inside app.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yourpassword@localhost/hostel_db'

5️⃣ Initialize the Database (if required)
python init_db.py

6️⃣ Run the Application
python app.py

7️⃣ Open the Application

Visit:

http://localhost:5000

🗂️ Project Structure
University-Hostel-Management-System/
│
├── app.py                # Main Flask app
├── models.py             # Database models and schema
├── init_db.py            # DB initialization script
├── requirements.txt      # Dependencies list
│
├── templates/            # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── add_student.html
│   ├── add_room.html
│   ├── add_payment.html
│   ├── add_staff.html
│   └── login.html
│
├── static/               # Static assets
│   ├── css/
│   ├── js/
│   └── images/
│
├── ddl_statements.sql    # DDL SQL script
├── dml_statements.sql    # DML SQL script
└── test_queries.sql      # SQL queries for validation

🧩 Database Schema
Table	Description
Student	Stores details like name, age, gender, contact, and course
Room	Holds information about room number, capacity, and occupancy
Block	Represents hostel blocks (A, B, etc.)
Allocation	Tracks which student is assigned to which room
Payment	Maintains payment records for each student
Staff	Contains staff member details and assigned roles
🧠 Normalization Summary

The database follows Third Normal Form (3NF) to remove redundancy and maintain consistency.

Each table has a primary key.

Foreign keys link related tables.

No transitive or partial dependencies exist.

🧾 Example Queries

Some sample queries used for testing:

-- Fetch students with pending payments
SELECT s.name, p.amount 
FROM student s 
LEFT JOIN payment p ON s.id = p.student_id 
WHERE p.status = 'Pending';

-- List all rooms and their occupancy status
SELECT room_no, capacity, occupied FROM room;

-- View allocations by block
SELECT b.block_name, s.name 
FROM allocation a
JOIN student s ON a.student_id = s.id
JOIN block b ON a.block_id = b.id;

📊 ER Diagram

The ER diagram visualizes entities like Student, Room, Staff, Block, Allocation, and Payment, and their relationships.

You can generate this in MySQL Workbench → Database → Reverse Engineer.

Future Enhancements

Online fee payment using Razorpay or PayPal

Email/SMS notifications for dues

Role-based access control (Warden, Accountant, Admin)

Advanced reporting and analytics module

🧑‍💻Author

Vaishnavi Aluvoju
🎓 JNTUH University College of Engineering, Manthani
🌐 GitHub: vaishnavi-aluvoju