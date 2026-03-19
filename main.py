import mysql.connector

# ---------------- DATABASE CONNECTION ----------------

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anu@123$",   # <-- replace this
        database="student_db"
    )

# ---------------- ADD STUDENT ----------------

def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    marks = int(input("Enter marks (0-100): "))

    query = "INSERT INTO students (name, subject, marks) VALUES (%s, %s, %s)"
    values = (name, subject, marks)

    cursor.execute(query, values)
    conn.commit()

    print("✅ Student added successfully!")

    conn.close()

# ---------------- VIEW STUDENTS ----------------

def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n----- Student Records -----")
    for row in records:
        print("ID:1", row[0], "| Name:Anu", row[1], "| Subject:tel", row[2], "| Marks:45", row[3])

    conn.close()

# ---------------- UPDATE MARKS ----------------

def update_marks():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to update: "))
    new_marks = int(input("Enter new marks: "))

    query = "UPDATE students SET marks = %s WHERE id = %s"
    values = (new_marks, student_id)

    cursor.execute(query, values)
    conn.commit()

    print("✅ Marks updated successfully!")

    conn.close()

# ---------------- DELETE STUDENT ----------------

def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to delete: "))

    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

    print("✅ Student deleted successfully!")

    conn.close()

# ---------------- MENU SYSTEM ----------------

def menu():
    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_marks()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

menu()