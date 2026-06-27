# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
# params: [[1, 2, 3], ['a', 'b', 'c']]  და # outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

params_1 = [[1, 2, 3], ["a", "b", "c"]]


def zip_list_1(x, y):
    return [str(pair) for pair in zip(x, y)]


print(f"{params_1} ელემენტების დაჯგუფებული სია არის: {zip_list_1 (*params_1)}")


# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError). ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.
# params:[1, 2, 3, 4, 5] და output: 120

from functools import reduce


def multiply_list(x):
    try:
        if not all(isinstance(item, (int, float)) for item in x):
            return "პარამეტრად უნდა გადაეცეს მხოლოდ რიცხვებისგან შემდგარი სია"
        return reduce(lambda x, y: x * y, x)
    except TypeError:
        return "პარამეტრად უნდა გადაეცეს მხოლოდ რიცხვებისგან შემდგარი სია"


params_2 = [1, 2, 3, 4, 5]


print(f"{params_2}-ის ელემენტების ნამრავლი არის:{multiply_list(params_2)}")


# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს. # params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

odd = lambda x: list(filter(lambda number: number % 2 == 1, x))

params_3 = [1, 2, 3, 4, 5, 6, 7]

print(f"{params_3}-ის კენტი ელემენტები არის:{odd(params_3)}")


# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით... # params: ['hello', 'world', 'coding', 'nod'], 'ing' # outputs: ['coding']


def func(x, y):
    try:
        return list(filter(lambda word: word.endswith(y), x))
    except TypeError:
        return "TypeError: პირველი პარამეტრი უნდა იყოს სტრინგების სია, ხოლო მეორე პარამეტრი სტრინგი"
    except Exception as ex:
        return f"დაფიქსირდა შეცდომა: {ex}"


params_4 = ["hello", "world", "coding", "nod"]
params_5 = "ing"


print(f"სიის ელემენტი, რომელიც მთავდება {params_5}-ზე არის {func(params_4, params_5)}")
