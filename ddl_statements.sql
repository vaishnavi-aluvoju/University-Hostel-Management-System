CREATE DATABASE HostelDB;
USE HostelDB;

CREATE TABLE Student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    department VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
);

CREATE TABLE Room (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_no VARCHAR(10) UNIQUE,
    block_name VARCHAR(50),
    capacity INT,
    occupancy INT DEFAULT 0
);

CREATE TABLE Allocation (
    allocation_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    room_id INT,
    allocation_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (room_id) REFERENCES Room(room_id)
);

CREATE TABLE Staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    designation VARCHAR(50),
    contact VARCHAR(15)
);

CREATE TABLE Payment (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);
