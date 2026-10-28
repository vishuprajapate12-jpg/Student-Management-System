import json
import os

if os.path.exists("students.json"):
    with open("students.json", "r") as file:
        students = json.load(file)
else:
    students = []

while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add student")
        name = input("Enter the name: ")
        roll_no = input("Enter the roll no: ")
        duplicate = False

        for student in students:
                 if student["roll_no"] == roll_no:
                    duplicate = True
                    break

        student = {
            "name": name,
            "roll_no": roll_no
        }

        students.append(student)

        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Student added and saved successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print(student["name"], student["roll_no"])

    elif choice == "3":
        name = input("Enter student name: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print(student["name"], student["roll_no"])
                found = True

        if not found:
            print("Student not found!")


    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
