-- List all students with their room details
SELECT s.name, r.room_no, r.block_name
FROM Student s
JOIN Allocation a ON s.student_id = a.student_id
JOIN Room r ON a.room_id = r.room_id;

-- List all unpaid students
SELECT s.name, p.amount, p.status
FROM Student s
LEFT JOIN Payment p ON s.student_id = p.student_id
WHERE p.status != 'Paid' OR p.status IS NULL;

-- Count available rooms
SELECT block_name, COUNT(*) AS available_rooms
FROM Room
WHERE occupancy < capacity
GROUP BY block_name;

-- Total payments received
SELECT SUM(amount) AS total_amount_collected FROM Payment;

-- View staff details
SELECT * FROM Staff;

