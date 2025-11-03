import sqlite3

# ------------------------------
# Connect Database
# ------------------------------
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# ------------------------------
# Create table (if not exists)
# ------------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
''')

conn.commit()

# ------------------------------
# Define Functions
# ------------------------------

def add_student(name, age, course, marks):
    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
                   (name, age, course, marks))
    conn.commit()
    print(" Student added successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n📋 All Students:")
    for row in rows:
        print(row)


def update_student(student_id, name, age, course, marks):
    cursor.execute('''
        UPDATE students
        SET name=?, age=?, course=?, marks=?
        WHERE id=?
    ''', (name, age, course, marks, student_id))
    conn.commit()
    print(" Record updated successfully!")


def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print(" Record deleted successfully!")


# ------------------------------
# Menu Interface
# ------------------------------
while True:
    print("""
=========== STUDENT MANAGEMENT ==========
1. Add New Student
2. View All Students
3. Update Student
4. Delete Student
5. Exit
========================================
""")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))
        add_student(name, age, course, marks)

    elif choice == '2':
        view_students()

    elif choice == '3':
        student_id = int(input("Enter student ID to update: "))
        name = input("New name: ")
        age = int(input("New age: "))
        course = input("New course: ")
        marks = float(input("New marks: "))
        update_student(student_id, name, age, course, marks)

    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)

    elif choice == '5':
        print(" Goodbye!")
        break

    else:
        print(" Invalid choice! Try again.")

# Close the connection at the end
conn.close()
