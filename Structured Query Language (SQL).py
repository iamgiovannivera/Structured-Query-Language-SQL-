# CREATE TABLE Artists (
#     artist_id INT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     birth_year INT
# );

# CREATE TABLE Genre (
#     genre_id INT PRIMARY KEY,
#     genre_name VARCHAR(255) NOT NULL
# );

# CREATE TABLE Albums (
#     album_id INT PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     artist_id INT,
#     genre_id INT,
#     release_year INT,
#     total_tracks INT,
#     FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
#     FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
# );



# Task 2: SQL Alteration


# ALTER TABLE Albums
# ADD COLUMN duration INT;


# Task 3: SQL Foreign Key Establishment


# ALTER TABLE Albums
# ADD CONSTRAINT fk_artist
# FOREIGN KEY (artist_id) REFERENCES Artists(artist_id);

# ALTER TABLE Albums
# ADD CONSTRAINT fk_genre
# FOREIGN KEY (genre_id) REFERENCES Genre(genre_id);


# 2. Managing a Fitness Center Database



# -- Inserting data into Members table
# INSERT INTO Members (id, name, age) VALUES
# (1, 'Jane Doe', 28),
# (2, 'John Smith', 35),
# (3, 'Emily Davis', 24);

# -- Inserting data into WorkoutSessions table
# INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES
# (1, 1, '2024-06-01', '07:00', 'Yoga'),
# (2, 2, '2024-06-01', '08:00', 'Cardio'),
# (3, 3, '2024-06-01', '09:00', 'Strength Training');



# -- Assuming Jane Doe's member_id is 1
# UPDATE WorkoutSessions
# SET session_time = '18:00'
# WHERE member_id = 1;



# -- Assuming John Smith's member_id is 2
# DELETE FROM Members
# WHERE id = 2;

# -- Ensure to delete related workout sessions if needed
# DELETE FROM WorkoutSessions
# WHERE member_id = 2;


# 3. SQL Query Exploration in Employee Database

# DDL for Creating Tables



# CREATE TABLE Departments (
#     department_id INT PRIMARY KEY,
#     department_name VARCHAR(100) NOT NULL
# );

# CREATE TABLE Employees (
#     employee_id INT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     age INT,
#     department_id INT,
#     FOREIGN KEY (department_id) REFERENCES Departments(department_id)
# );


# Task 1: SQL DISTINCT Usage



# SELECT DISTINCT department_name
# FROM Departments
# JOIN Employees ON Departments.department_id = Employees.department_id;

# Task 2: SQL COUNT Functionality


# SELECT department_name, COUNT(*) AS total_employees
# FROM Departments
# JOIN Employees ON Departments.department_id = Employees.department_id
# GROUP BY department_name;


# Task 3: SQL BETWEEN Usage


# SELECT name, age, department_id
# FROM Employees
# WHERE age BETWEEN 25 AND 30;