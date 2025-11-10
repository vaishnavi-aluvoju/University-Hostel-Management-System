INSERT INTO Student (name, age, gender, department, email, phone)
VALUES 
('Vaishnavi Aluvoju', 21, 'Female', 'CSE', 'vaishnavi@jntuh.ac.in', '9876543210'),
('Sidhu Kumar', 22, 'Male', 'ECE', 'sidhu@jntuh.ac.in', '8765432109');

INSERT INTO Room (room_no, block_name, capacity, occupancy)
VALUES 
('A101', 'Block A', 2, 1),
('A102', 'Block A', 2, 0);

INSERT INTO Allocation (student_id, room_id, allocation_date)
VALUES (1, 1, '2025-11-05');

INSERT INTO Staff (name, designation, contact)
VALUES ('Ravi Teja', 'Warden', '9876501234');

INSERT INTO Payment (student_id, amount, payment_date, status)
VALUES (1, 5000, '2025-11-08', 'Paid');
