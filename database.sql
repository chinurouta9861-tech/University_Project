CREATE DATABASE university;

USE university;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    gender VARCHAR(20),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    course VARCHAR(50),
    interests VARCHAR(200),
    password VARCHAR(100),
    security_question VARCHAR(200),
    security_answer VARCHAR(200)
);