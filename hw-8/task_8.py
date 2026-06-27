# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


user_input_1 = input(
    "შეიყვანე სასურველი რიცხვი ციფრებით და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას: "
)

if user_input_1.isdigit():
    n = int(user_input_1)
    for i in range(n):
        print(fibonacci(i))
else:
    print("შეიყვანეთ დადებითი მთელი რიცხვი ციფრებით")


# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.


def is_anagram(word_1, word_2):
    return sorted(word_1) == sorted(word_2)


word_1 = input("შეიყვანე პირველი სიტყვა: ").lower().strip()
word_2 = input("შეიყვანე მეორე სიტყვა: ").lower().strip()
if word_1 == word_2:
    print(f"{word_1} და {word_2} სრულიად იდენტური სიტყვებია")
elif is_anagram(word_1, word_2):
    print(f"{word_1} და {word_2} არის ანაგრამები")
else:
    print(f"{word_1} და {word_2} არ არის ანაგრამები")


# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


user_input_3 = input("შეიყვანეთ სასურველი რიცხვი და გამოგიტან ამ რიცხვის ფაქტორიალს: ")

if user_input_3.isdigit():
    n = int(user_input_3)
    print(f"{n}-ის ფაქტორიალის არის: {factorial(n)}")
else:
    print("შეიყვანეთ დადებითი მთელი რიცხვი ციფრებით!")


# 4. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.


def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count


user_input_4_1 = input("შეიყვანეთ სასურველი სტრიქონი: ")
user_input_4_2 = input(
    "შეიყვანეთ სასურველი სიმბოლო, რომლის ნახვაც გინდათ, სტრიქონში რამდენჯერ მეორდება: "
)

print(
    f"{user_input_4_2}-ს რაოდენობა სტრიქონში არის: {count_occurrences(user_input_4_1, user_input_4_2)}"
)
