# 1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y. კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ ვექტორების დამატება და __str__ მეთოდი, რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".

# მაგალითად:
# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v1)
# print(v1)
# print(v3)

# # Output:
# (2, 3)
# (3, 4)
# (5, 7)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, self_2):
        return Vector(self.x + self_2.x, self.y + self_2.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2

print("=" * 30)
print("დავალება 1")
print("=" * 30)

print(v1, "\n")
print(v2, "\n")
print(v3, "\n")

# 2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს ორი წიგნის ტოლობას.
# ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

# მაგალითად:
# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  # Output: True
# print(book1 == book3)  # Output: False


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, self_2):
        return self.title == self_2.title and self.author == self_2.author


book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Brave New World", "Aldous Huxley")

print("=" * 30)
print("დავალება 2")
print("=" * 30)

print(
    f"{book1.title} {book1.author} და {book2.title} {book2.author} არის იდენტური ? {book1 == book2}",
    "\n",
)
print(
    f"{book1.title} {book1.author} და {book3.title} {book3.author} არის იდენტური ? {book1 == book3}",
    "\n",
)

# 3. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.

# Car კლასს დაუმატეთ  თითოეული ატრიბუტისთვის set და get თვისებები მათი ცვლილებებისთვის.

# დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის მთელი და ა.შ.


from datetime import datetime


class Car:
    number_of_cars = 0

    def __new__(cls, brand, model, year):
        instance = super().__new__(cls)
        cls.number_of_cars += 1
        return instance

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or not value.strip():
            raise TypeError("Brand must be a string")
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str) or not value.strip():
            raise TypeError("Model must be a string")
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError("Year must be a positive integer")
        if value > datetime.now().year:
            raise ValueError("Year cannot be in the future")
        self._year = value

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

    @classmethod
    def total_cars(cls):
        return cls.number_of_cars


print("=" * 40)
print("დავალება 3")
print("=" * 40)

car_1 = Car("Porche", "911", 1961)
car_2 = Car("Mercedes", "AMG", 2026)
car_3 = Car("Lotus", "Evija", 2026)

print(car_1, "\n")
print(car_2, "\n")
print(car_3, "\n")

print("-" * 40)
print(f"Total number of cars: {Car.total_cars()}")
