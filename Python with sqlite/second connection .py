import sqlite3

# ------------------------------
# Connect Database
# ------------------------------
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# ------------------------------
# Create table (if not exists)
# ------------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    salary INTEGER,
    experience REAL
)
''')
conn.commit()

# ------------------------------
# Define Functions
# ------------------------------

def add_employees(name, department, salary, experience):
    cursor.execute("INSERT INTO employees (name, department, salary, experience) VALUES (?, ?, ?, ?)",
                   (name, department, salary, experience))
    conn.commit()
    print("Employee added successfully!")


def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print("\nAll employees:")
    for row in rows:
        print(row)


def update_employees(employee_id, name, department, salary, experience):
    cursor.execute('''
        UPDATE employees
        SET name=?, department=?, salary=?, experience=?
        WHERE id=?
    ''', (name, department, salary, experience, employee_id))
    conn.commit()
    print("Record updated successfully!")


def delete_employee(employee_id):
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    conn.commit()
    print(" Record deleted successfully!")


# ------------------------------
# Menu Interface
# ------------------------------
while True:
    print("""
=========== EMPLOYEE MANAGEMENT ===========
1. Add New Employee
2. View All Employees
3. Update Employee
4. Delete Employee
5. Exit
===========================================
""")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        department = input("Enter department: ")
        salary = int(input("Enter salary: "))
        experience = float(input("Enter experience (in years): "))
        add_employees(name, department, salary, experience)

    elif choice == '2':
        view_employees()

    elif choice == '3':
        employee_id = int(input("Enter employee ID to update: "))
        name = input("New name: ")
        department = input("New department: ")
        salary = int(input("New salary: "))
        experience = float(input("New experience: "))
        update_employees(employee_id, name, department, salary, experience)

    elif choice == '4':
        employee_id = int(input("Enter employee ID to delete: "))
        delete_employee(employee_id)

    elif choice == '5':
        print(" Goodbye!")
        break

    else:
        print(" Invalid choice! Try again.")

# Close the connection at the end
conn.close()
