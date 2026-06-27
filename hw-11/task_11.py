import json, os

chess_players = [
    {"id": 19, "name": "Jobava", "country": "Georgia", "rating": 2588, "age": 41},
    {"id": 28, "name": "Caruana", "country": "USA", "rating": 2781, "age": 32},
    {"id": 35, "name": "Giri", "country": "Netherlands", "rating": 2771, "age": 30},
    {"id": 84, "name": "Carlsen", "country": "Norway", "rating": 2864, "age": 34},
    {"id": 118, "name": "Ding", "country": "China", "rating": 2799, "age": 32},
    {"id": 139, "name": "Karjakin", "country": "Russia", "rating": 2747, "age": 35},
    {"id": 258, "name": "Duda", "country": "Poland", "rating": 2731, "age": 31},
    {"id": 301, "name": "Vachier-Lagrave", "country": "France", "rating": 2737,"age": 34},
    {"id": 403, "name": "Nakamura", "country": "USA", "rating": 2768, "age": 36},
]


# 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის სახელს და დააბრუნებს ფაილის სრულ გზას.
def get_file_path(file_name):
    folder = "chess_file"
    os.makedirs(folder, exist_ok=True)
    folder_path = os.path.join(folder, file_name)

    with open(folder_path, mode="w", encoding="utf-8") as file:
        json.dump(chess_players, file, indent=4)

    return os.path.abspath(folder_path)


full_path = get_file_path("chess_players.json")

print(f"ფაილის სრული გზა არის: {full_path}")

print()

# 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.


def read_file(file_name):
    if not os.path.exists(file_name):
        return "აღნიშნული ფაილი არ არსებობს"
    with open(file_name, mode="r", encoding="utf-8") as file:
        return json.load(file)


data = read_file(full_path)
pretty_data = json.dumps(data, indent=4)

print(pretty_data)

print()


# 3. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და დაამატებს ფაილის კონტენტს.

# [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]

# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.

add_chess_players = [
    {"id": 568, "name": "Kasparov", "country": "Russia", "rating": 2705, "age": 56},
    {"id": 189, "name": "Karpov", "country": "Russia", "rating": 2698, "age": 59},
]


def add_file(file_name: str, json_data: dict):
    data_2 = read_file(file_name)

    if type(json_data) == dict:
        for player in data_2:
            if player["id"] == json_data["id"]:
                print(f"ჭადრაკის მოთამაშე {json_data['id']} აიდით, უკვე არსებობს")
                break
        else:
            data_2.append(json_data)
            with open(file_name, mode="w", encoding="utf-8") as file:
                json.dump(data_2, file, indent=4)
                print(
                    f"ახალი მოთამაშე {json_data['name']} {json_data['id']} აიდით დამატებულია ფაილში"
                )
    else:
        print("ფაილის განსაახლებლად საჭიროა გადაცემულ იქნას ლექსიკონი!")


for new_player in add_chess_players:
    add_file(full_path, new_player)

print()

# 4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.


def update_file(file_name: str, player_id: int, updates: dict):
    data_3 = read_file(file_name)

    for player in data_3:
        if player["id"] == player_id:
            player.update(updates)
            with open(file_name, mode="w", encoding="utf-8") as file:
                json.dump(data_3, file, indent=4)
            print(f"{player['name']}-ის მონაცემები {player_id} აიდით განახლებულია")
            break
    else:
        print(f"{player_id} აიდით მონაცემები არ არსებობს")


while True:
    try:
        rating_id = int(
            input("შეიყვანეთ იმ მოთამაშის აიდი რომლის მონაცემების განახლებაც გინდათ: ")
        )
        rating_input = int(input("შეიყვანეთ განახლებული რეიტინგი: "))
        age_input = int(input("შეიყვანეთ განახლებული ასაკი: "))
        update_data = {"rating": rating_input, "age": age_input}
        update_file(full_path, rating_id, update_data)
        break
    except ValueError:
        print("გთხოვთ შეიყვანეთ მთელი რიცხვები ციფრებით!")

print()
