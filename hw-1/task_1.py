# 1. კონსოლიდან შეიტანეთ ორი რიცხვი და დაბეჭდეთ ყველა არითმეტიკული ოპერაცია (მიმატება, გამოკლება, გამრავლება, ჩვეულებრივი გაყოფა, მთელზე გაყოფა, ნაშთის აღება, ახარისხება).

number_1 = 25
number_2 = 4

print(number_1 + number_2)  # მიმატება
print(number_1 - number_2)  # გამოკლება
print(number_1 * number_2)  # გამრავლება
print(number_1 / number_2)  # ჩვეულებრივი გაყოფა
print(number_1 // number_2)  # მთელზე გაყოფა
print(number_1 % number_2)  # ნაშთის აღება
print(number_1**number_2)  # ახარისხება


# 2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

diagonal_1 = eval(input("შეიყვანე რომბის პირველი დიაგონალის სიგრძე სანტიმეტრებში: "))
diagonal_2 = eval(input("შეიყვანე რომბის მეორე დიაგონალის სიგრძე სანტიმეტრებში: "))

area_of_rhombus = (diagonal_1 * diagonal_2) / 2

print(f"რომბის ფართობი არის: {area_of_rhombus} სმ")


# 3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში.

metres = eval(input("შეიყვანე მეტრების რაოდენობა: "))

centimeter = metres * 100
decimeter = metres * 10
millimeter = metres * 1000
mile = metres * 1609.34

print(f"{metres} მეტრი არის: {centimeter} სმ")
print(f"{metres} მეტრი არის: {decimeter} დმ")
print(f"{metres} მეტრი არის: {millimeter} მმ")
print(f"{metres} მეტრი არის: {mile} მილი")


# 4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.

base_of_triangle = eval(input("შეიყვანე სამკუთხედის ფუძის სიგრძე რიცხვებში: "))
height_of_triangle = eval(input("შეიყვანე სამკუთხედის სიმაღლე რიცხვებში: "))

area_of_triangle = (base_of_triangle * height_of_triangle) / 2

print(f"სამკუთხედის ფართობი არის: {area_of_triangle} სმ")


# 5. კონსოლიდან შეიტანეთ ორნიშნა რიცხვი და დაბეჭდეთ ციფრთა ჯამი.

console_number = eval(input("შეიყვანე ორნიშნა რიცხვი ციფრებით: "))

digit_1 = console_number // 10
digit_2 = console_number % 10

print(f"შეყვანილი ორნიშნა რიცხვის ციფრთა ჯამი არის: {digit_1 + digit_2}")
