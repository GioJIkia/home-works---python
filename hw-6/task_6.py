# TODO
# დაწერეთ პროგრამა, რომელიც ტერმინალში მომხმარებელს გამოუტანს სტუდენტების აიდის (id) სიას, მომხარებელი აირჩევს სტუდენტის აიდის, მიღებული აიდისთვის დაბეჭდავს სტუდენტის მონაცემებს. მონაცემებში უნდა დაიბეჭდოს (სახელი, გვარი, ასაკი და ქულა თითოეული საგნის მიხედვით). მაგალითად: მომხარებელმა თუ აირჩია სტუდენტი აიდით 20, უნდა დაბეჭდოთ ამ სტუდენტის ინფომრაცია.

# terminal ouput:
# studentebis ID: 20, 25, 56, 100, 1232, 846723
# airchiet studentis ID:
# შემდეგ მომხარებელს შეყავს აიდი, მაგალითად  - 20

# პროგრამა ბეჭდავს ტერმინალში შემდეგ ინფორმაციას (output):

# student infomration:
# ID: 20, Name: Giorgi, Age: 25
# subject: Math, grade: B
# subject: Physics, grade: A
# subject: English, grade: A
# subject: Chemistry, grade: B
# subject: History, grade: c

my_dict = {
    "students": [
        {"id": 20, "name": "Giorgi", "age": 25},
        {"id": 25, "name": "Giorgi", "age": 23},
        {"id": 56, "name": "Nika", "age": 25},
        {"id": 100, "name": "Nika", "age": 22},
        {"id": 1232, "name": "Dato", "age": 22},
        {"id": 846723, "name": "Archili", "age": 32},
    ],
    "subjects": [
        {
            "id": 1,
            "name": "Math",
            "grades": {
                "20": "B",
                "25": "A",
                "56": "B",
                "100": "A",
                "1232": "C",
                "846723": "A",
            },
        },
        {
            "id": 2,
            "name": "Physics",
            "grades": {
                "20": "A",
                "25": "B",
                "56": "B",
                "100": "A",
                "1232": "C",
                "846723": "B",
            },
        },
        {
            "id": 3,
            "name": "English",
            "grades": {
                "20": "A",
                "25": "A",
                "56": "A",
                "100": "A",
                "1232": "B",
                "846723": "A",
            },
        },
        {
            "id": 4,
            "name": "Chemistry",
            "grades": {
                "20": "B",
                "25": "B",
                "56": "B",
                "100": "A",
                "1232": "A",
                "846723": "A",
            },
        },
        {
            "id": 5,
            "name": "History",
            "grades": {
                "20": "C",
                "25": "B",
                "56": "B",
                "100": "A",
                "1232": "A",
                "846723": "A",
            },
        },
    ],
}

id_list = []

for student in my_dict["students"]:
    id_list.append(str(student["id"]))

print(f"სტუდენტების ID: {', '.join(id_list)}")

user_input = input(f"აირჩე სასურველი სტუდენტის ID: ")

while user_input not in id_list:
    user_input = input(
        f"თქვენს მიერ შეყვანილია არასწორი ID, აირჩე სასურველი სტუდენტის ID სიიდან: "
    )


print(f"\n{'=' * 47}")
print(f"  {'ID':<6}{'Student':<12}{'age':<8}{'Subject':<12}{'Grade'}")
print("=" * 47)

for student in my_dict["students"]:
    if student["id"] == int(user_input):
        student_name = student["name"]
        student_age = student["age"]
        break

current_id = user_input
current_name = student_name
current_age = student_age

for subject in my_dict["subjects"]:
    if user_input in subject["grades"]:
        subject_name = subject["name"]
        subject_grade = subject["grades"][user_input]
        print(
            f"{current_id:<6}{current_name:<12}{current_age:<8}{subject_name:<12}{subject_grade}"
        )

        current_id = ""
        current_name = ""
        current_age = ""
