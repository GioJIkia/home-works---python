# ; 1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს რიცხვს პარამეტრად და გლობალურ int_list
# ; სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

int_list = [10, 20, 30, 40]


def add(x):
    int_list.append(x)


user_input_1 = input("შეიყვანეთ სასურველი რიცხვი სიაში დასამატებლად: ")

if user_input_1.isdigit():
    user_input_1 = int(user_input_1)

    if user_input_1 not in int_list:
        add(user_input_1)
    else:
        print("გთხოვთ შეიყვანოთ სხვა რიცხვი, ეს რიცხვი არის უკვე სიაში!")
        exit()
else:
    print("გთხოვთ შეიყვანოთ რიცხვი ციფრებით!")
    exit()

print("განახლებული სია:", int_list)

print()

# ; 2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].


def sum_list(list):
    sum_numbers = 0
    for i in list:
        sum_numbers += i
    return sum_numbers


list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

print("სიაში მოცემული რიცხვების ჯამი არის:", sum_list(list))

print()

# ; 3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ
#  ცვლადს აქვს  (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას.

gl_str = "Global"


def global_str():
    gl_str = "Local"
    return gl_str


print("ლოკალური ცვლადის მნიშვნელობა:", global_str())
print("გლობალური ცვლადის მნიშვნელობა:", gl_str)

print()


# ; 4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).


def sum_of_numbers_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_numbers_digits(number // 10)


user_input_2 = input("შეიყვანეთ სასურველი რიცხვი, რომელთა ციფრთა ჯამიც გაინტერესებთ: ")
if user_input_2.isdigit():
    user_input_2 = int(user_input_2)
    result = sum_of_numbers_digits(user_input_2)
    print(f"თქვენს მიერ შეყვანილი რიცხვის ციფრების ჯამი არის: {result}")
else:
    print("გთხოვთ შეიყვანოთ დადებითი რიცხვი ციფრებით!")

print()

# ; 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად  input: Hello   Output: olleH)


def reverse_string(string):
    if len(string) <= 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


user_input_3 = input("შეიყვანეთ სასურველი სტრიქონი რომლის შებრუნებაც გინდათ: ")

if len(user_input_3) == 0:
    print("თქვენ არაფერი შეგიყვანიათ, გთხოვთ შეიყვანოთ სასურველი სტრიქონი!")
else:
    print(
        f"თქვენს მიერ შეყვანილი სტრიქონის შებრუნების სტრიქონი არის: {reverse_string(user_input_3)}"
    )
