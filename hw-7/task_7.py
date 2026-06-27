# დავალება 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).

user_input_1 = input("შეიყვანეთ სასურველი მიმდევრობა: ").strip()

while len(user_input_1) == 0 or not user_input_1.isdigit():
    user_input_1 = input(
        "გთხოვთ შეიყვანეთ სასურველი მიმდევრობა, ციფრების გამოყენებით: "
    ).strip()
else:
    unique_set_1 = set(int(i) for i in user_input_1)
    print("უნიკალური მონაცემების სიმრავლე:", unique_set_1)

print()


# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, რომლის შეცვლაც შეუძლებელი იქნება (frozenset).

user_input_2 = input("შეიყვანეთ სასურველი მიმდევრობა: ").strip()

while not user_input_2.isdigit():
    user_input_2 = input(
        "გთხოვთ შეიყვანეთ სასურველი მიმდევრობა, ციფრების გამოყენებით: "
    ).strip()
else:
    unique_set_2 = frozenset(int(i) for i in user_input_2)
    print("უნიკალური მონაცემების სიმრავლე, რომლის შეცვლაც შეუძლებელია:", unique_set_2)

print()


# 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).

set_1 = {1, 2, 3, 4, 5}
set_2 = {5, 6, 7, 8, 9, 10}

print("გაერთიანებული მონაცემები კორტეჟის სახით:", tuple(set_1.union(set_2)), "\n")

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).

user_input_3 = input("შეიყვანეთ სასურველი მიმდევრობა, ციფრების გამოყენებით: ").strip()

while not user_input_3.isdigit():
    user_input_3 = input(
        "გთხოვთ შეიყვანეთ სასურველი მიმდევრობა, ციფრების გამოყენებით: "
    ).strip()
else:
    input_tuple = tuple(int(i) for i in user_input_3)
    print("კონსოლიდან შეტანილი რიცხვების მიმდევრობა როგორც კორტეჟი:", input_tuple)

    unique_list_3 = list(set(input_tuple))
    print("უნიკალური ელემენტების სია:", unique_list_3)


print()

# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს: [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# დაბეჭდეთ შემდეგი ფორმატით:
# Name: Gega, Age: 24
# Name: Gaga, Age: 21
# Name: Goga, Age: 19
# Name: Giga, Age: 27
# Name: Gagi, Age: 11

users = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for name, age in users:
    print(f"Name: {name}, Age: {age}")

print()


# 6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"]. ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"] დავბეჭდოთ თანხვედრა.

users_1 = ["Irakli", "Giorgi", "Nona", "Oto"]

users_2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

print("მომხმარებლების სიის თანხვედრა: ", set(users_1).intersection(set(users_2)))
