# 1 შექმენით csv ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,mark
# 1,string,0,string,string,0
# 2,string,0,string,string,0

import os, csv

folder = "csv"
file_name = "students.csv"

students = [
    {
        "id": 8,
        "name": "Nika",
        "age": 19,
        "grade": "B",
        "subject_name": "Physic",
        "mark": 87,
    },
    {
        "id": 19,
        "name": "Nuca",
        "age": 18,
        "grade": "B",
        "subject_name": "Mathematic",
        "mark": 84,
    },
    {
        "id": 11,
        "name": "Archil",
        "age": 21,
        "grade": "C",
        "subject_name": "Mathematic",
        "mark": 74,
    },
    {
        "id": 25,
        "name": "Nino",
        "age": 20,
        "grade": "A",
        "subject_name": "Informatic",
        "mark": 95,
    },
    {
        "id": 22,
        "name": "Giga",
        "age": 20,
        "grade": "A",
        "subject_name": "Biology",
        "mark": 81,
    },
    {
        "id": 31,
        "name": "Lana",
        "age": 22,
        "grade": "B",
        "subject_name": "Geography",
        "mark": 88,
    },
    {
        "id": 3,
        "name": "Nino",
        "age": 23,
        "grade": "B",
        "subject_name": "Informatic",
        "mark": 85,
    },
]

os.makedirs(folder, exist_ok=True)
file_name = os.path.join(folder, file_name)

with open(file_name, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)


# 2. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი სტუდენტს დაამატებს csv ფაილში.
#    დაასორტირეთ მონაცემები id-ის მიხედვით.


def add_student_to_csv(student):
    while True:
        user_input_add = input(
            "Enter student details to add (id,name,age,grade,subject_name,mark): "
        )
        try:
            add_detaiLs = [item.strip() for item in user_input_add.split(",")]
            new_student = {
                "id": int(add_detaiLs[0]),
                "name": add_detaiLs[1],
                "age": int(add_detaiLs[2]),
                "grade": add_detaiLs[3],
                "subject_name": add_detaiLs[4],
                "mark": int(add_detaiLs[5]),
            }
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid student details.")
            continue

        all_students = []

        with open(file_name, mode="r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["age"] = int(row["age"])
                row["mark"] = int(row["mark"])
                all_students.append(row)

        if new_student["id"] in [student["id"] for student in all_students]:
            print("ID already exists. Please enter a different ID.")
            continue
        if new_student["age"] < 0 or new_student["mark"] < 0 or new_student["id"] < 0:
            print(
                "Invalid input. Please enter valid student details, age and mark and id must be positive."
            )
            continue
        break

    all_students.append(new_student)
    all_students.sort(key=lambda x: x["id"])
    with open(file_name, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=all_students[0].keys())
        writer.writeheader()
        writer.writerows(all_students)
        print(f"Student {new_student ['name']} added successfully")


add_student_to_csv(students)

# 3. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა,
#    ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.


def read_students_from_csv():
    students = []
    with open(file_name, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["age"] = int(row["age"])
            row["mark"] = int(row["mark"])
            students.append(row)
    return students


while True:
    print("\nChoose an option:")
    print("1. View ALL students")
    print("2. View a SPECIFIC student by ID")
    print("3. Exit")
    choice = input("Enter option (1, 2 or 3): ").strip()

    if choice == "1":
        students = read_students_from_csv()
        w1 = 40
        w2 = 10
        lines = w1 + w2 + 20
        header = tuple(students[0].keys())

        print()
        print("=" * lines)
        print(
            f"  {header[0]:<{w2}} {header[1]:<{w2}} {header[2]:<{w2}} {header[3]:<{w2}} {header[4]:<{15}} {header[5]}"
        )
        for student in students:

            print("-" * lines)
            print(
                f"  {student['id']:<{w2}} {student['name']:<{w2}} {student['age']:<{w2}} {student['grade']:<{w2}} {student['subject_name']:<{15}} {student['mark']}"
            )

    elif choice == "2":
        students = read_students_from_csv()
        try:
            search_id = int(input("Enter the ID of the student you want to view: "))
        except ValueError:
            print("Invalid input. ID must be a number.")
            continue

        w1 = 40
        w2 = 10
        lines = w1 + w2 + 20
        header = tuple(students[0].keys())

        print()
        print("=" * lines)
        print(
            f"  {header[0]:<{w2}} {header[1]:<{w2}} {header[2]:<{w2}} {header[3]:<{w2}} {header[4]:<{15}} {header[5]}"
        )
        for student in students:
            if student["id"] == search_id:
                print("-" * lines)
                print(
                    f"  {student['id']:<{w2}} {student['name']:<{w2}} {student['age']:<{w2}} {student['grade']:<{w2}} {student['subject_name']:<{15}} {student['mark']}"
                )
                break
        else:
            print(f"Student with ID {search_id} not found.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1, 2 or 3")

print()

# 4. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.


def calculate_average_mark(students):
    students = read_students_from_csv()

    subject_marks = {}

    for student in students:
        subject = student["subject_name"]
        mark = student["mark"]

        if subject not in subject_marks:
            subject_marks[subject] = []

        subject_marks[subject].append(mark)
    for subject, marks in subject_marks.items():
        average_mark = int(sum(marks) / len(marks))
        print(f"The average mark for {subject} is: {average_mark}")


calculate_average_mark(students)

print()

# 5. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის `id`,
#    საგანს და განახლებულ ქულას.


def update_student_mark():
    students = read_students_from_csv()

    while True:
        try:
            student_id = int(input("Enter the ID of the student you want to update: "))
            subject_name = input("Enter the subject name: ").strip()
            new_mark = int(input("Enter the new mark for the student: "))

            if student_id < 0 or new_mark < 0:
                print("ID and mark must be positive numbers.")
                continue
        except ValueError:
            print("Invalid input. ID and mark must be numbers.")
            continue

        updated = False
        for student in students:
            if (
                student["id"] == student_id
                and student["subject_name"].lower() == subject_name.lower()
            ):
                student["mark"] = new_mark
                updated = True
                break
        if updated:
            break
        else:
            print(
                f"No student found with ID {student_id} for subject '{subject_name}'. Please try again."
            )

    with open(file_name, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)

    print(
        f"Student ID {student_id}'s mark for '{subject_name}' updated successfully to {new_mark}!"
    )


update_student_mark()

print()

# 6. დაამატეთ ახალი სტუდენტი და ჩაწერეთ ფაილში.
new_student = {
    "id": 5,
    "name": "Demetre",
    "age": 18,
    "grade": "A",
    "subject_name": "Informatic",
    "mark": 94,
}

all_students = read_students_from_csv()
all_students.append(new_student)
all_students.sort(key=lambda student: student["id"])

with open(file_name, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=all_students[0].keys())
    writer.writeheader()
    writer.writerows(all_students)

print(
    f"New student {new_student['name']} of {new_student['id']} ID added successfully!"
)
