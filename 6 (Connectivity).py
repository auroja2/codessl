import mysql.connector

# Function to connect to the MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="123456789",  # Replace with your MySQL password
        database="sample_db"  # Replace with your database name
    )

# Function to add a student to the database
def add_student(name, age, grade):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
    conn.commit()
    print("Student added successfully!")
    cursor.close()
    conn.close()

# Function to update a student's details in the database
def update_student(id, name, age, grade):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s", (name, age, grade, id))
    conn.commit()
    print("Student updated successfully!")
    cursor.close()
    conn.close()

# Function to delete a student from the database
def delete_student(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    print("Student deleted successfully!")
    cursor.close()
    conn.close()

# Function to view all students in the database
def view_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

# Main section to test the functions
if __name__ == "__main__":
    # Example usage
    add_student("John Doe", 20, "A")  # Add student
    update_student(1, "John Doe", 21, "A+")  # Update student with ID 1
    view_students()  # View all students
   # delete_student(1)  # Delete student with ID 1


# pip3 install mysql-connector-python

'''
sudo mysql -u root -p
CREATE DATABASE sample_db;
USE sample_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(5)
);
'''