# 1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. ასევე, შექმენით მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

# 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს. ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.

# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ელემენტის ხანგრძლივობა შეადგენს [battery_life] საათს".

# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას.

# 5. Car კლასს დაამატეთ კლასის მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.


from datetime import datetime


class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.number_of_cars += 1

    def age_of_car(self):

        current_year = datetime.now().year
        age = current_year - self.year
        return age

    def car_info(self):
        print(
            f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Age: {self.age_of_car()} years"
        )

    @classmethod
    def total_cars(cls):
        print(f"Total number of cars: {cls.number_of_cars}")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"{self.brand} {self.model} life of battery is {self.battery_life} hours")


print("*" * 30)
print("please enter details of cars!")
print("*" * 30)
print()

all_cars = []

while True:

    while True:
        brand = input("enter the brand of the car: ").strip().capitalize()
        if brand == "" or brand.isdigit():
            print("Error:please enter correct brand of the car")
        else:
            break

    print()

    while True:
        model = input("enter the model of the car: ").strip().capitalize()
        if model == "":
            print("Error:please enter model of the car")
        else:
            break

    print()

    while True:
        try:
            year = int((input("enter the manufacturing year of the car: ")).strip())
            current_year = datetime.now().year

            if year < 0 or year > current_year:
                print("Error: please enter correct year of the car")
            else:
                break
        except ValueError:
            print("Error: please enter correct year of the car")

    print()

    while True:
        electric_car_or_not = input("is the car electric? (yes/no): ").strip().lower()

        print()

        if electric_car_or_not == "yes":
            while True:
                try:
                    battery_life = int(
                        (input("enter the battery life of the car by hours: ")).strip()
                    )
                    if battery_life <= 0:
                        print("Error: please enter correct battery life of the car")
                    else:
                        break
                except ValueError:
                    print("Error: please enter correct battery life of the car")

            print()

            new_car = ElectricCar(brand, model, year, battery_life)
            print("-" * 40)
            all_cars.append(new_car)
            print(f"{new_car.brand} {new_car.model} added to the list")
            print()
            print(f"Total number of cars: {Car.number_of_cars}")
            print("-" * 40)
            print()
            new_car.battery_info()
            print()
            break
        elif electric_car_or_not == "no":
            new_car = Car(brand, model, year)
            print("-" * 40)
            all_cars.append(new_car)
            print(f"{new_car.brand} {new_car.model} added to the list")
            print()
            print(f"Total number of cars: {Car.number_of_cars}")
            print("-" * 40)
            print()
            break
        else:
            print("Error: please enter only yes or no")
            print()

    should_continue = True
    while True:
        continue_input = (
            input("Do you want to enter another car details? (yes/no): ")
            .strip()
            .lower()
        )

        if continue_input == "yes":
            break
        elif continue_input == "no":
            should_continue = False
            break
        else:
            print("Error: please enter only yes or no")
            print()

    print()
    if not should_continue:
        break

print("=" * 65)
print("All cars which is in the list")
print("-" * 65)
print(f"{'Brand':<15}{'Model':<15}{'Year':<10} {'Age':<10} {'Battery life'}")
print("-" * 65)
for car in all_cars:

    if isinstance(car, ElectricCar):
        print(
            f"{car.brand:<15}{car.model:<15}{car.year:<10} {car.age_of_car():<10} {car.battery_life} hours"
        )
    else:
        print(f"{car.brand:<15}{car.model:<15}{car.year:<10} {car.age_of_car()}")

print("=" * 65)
Car.total_cars()
