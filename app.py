from datetime import datetime

class Animals:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")

class Pets(Animals):
    def __init__(self, name, birth_date, commands):
        super().__init__(name, birth_date)
        self.commands = commands

    def get_commands(self):
        return self.commands

    def set_commands(self, new_commands):
        self.commands = new_commands

class Dogs(Pets):
    pass

class Cats(Pets):
    pass

class Hamsters(Pets):
    pass

class Horses(Animals):
    pass

class Camels(Animals):
    pass

class Donkeys(Animals):
    pass


animals_list = []


def main():
    choice = -1
    while choice != 0:
        print_menu()
        try:
            choice = int(input("Выберите пункт меню: "))
        except ValueError:
            print("Неверный формат ввода. Введите целое число.")
            continue

        if choice == 1:
            add_new_animal()
        elif choice == 2:
            list_commands()
        elif choice == 3:
            train_animal()
        elif choice == 4:
            sort_animals_by_birth_date()
        elif choice == 5:
            print_total_animals_count()
        elif choice == 0:
            print("Выход")
        else:
            print("Неправильный выбор")

        print()


def print_menu():
    print("Меню:")
    print("1. Добавить новое животное")
    print("2. Список команд животного")
    print("3. Обучение новым командам")
    print("4. Вывести список животных по дате рождения")
    print("5. Вывести общее количество животных")
    print("0. Выход")


def add_new_animal():
    name = input("Введите имя животного: ")
    birth_date = input("Введите дату рождения животного: ")
    try:
        animal_type = int(input("Выберите тип животного: 1 - Собака, 2 - Кошка, 3 - Хомяк, 4 - Лошадь, 5 - Верблюд, 6 - Осел: "))
    except ValueError:
        print("Неверный формат ввода. Введите целое число.")
        return

    animal = None

    if animal_type == 1:
        animal = Dogs(name, birth_date, [])
    elif animal_type == 2:
        animal = Cats(name, birth_date, [])
    elif animal_type == 3:
        animal = Hamsters(name, birth_date, [])
    elif animal_type == 4:
        animal = Horses(name, birth_date)
    elif animal_type == 5:
        animal = Camels(name, birth_date)
    elif animal_type == 6:
        animal = Donkeys(name, birth_date)

    if animal:
        animals_list.append(animal)
    else:
        print("Неправильный выбор")


def list_commands():
    name = input("Введите имя животного: ")

    for animal in animals_list:
        if animal.name == name:
            if isinstance(animal, Pets):
                commands = animal.get_commands()
                print(f"Список команд для животного {name}:")
                for command in commands:
                    print(command)
            else:
                print(f"У животного {name} нет команд")
            return

    print(f"Животное с именем {name} не найдено")


def train_animal():
    name = input("Введите имя животного: ")

    for animal in animals_list:
        if animal.name == name:
            if isinstance(animal, Pets):
                new_command = input(f"Введите новую команду для животного {name}: ")
                animal.set_commands(animal.get_commands() + [new_command])
                print(f"Животное {name} успешно обучено новой команде")
            else:
                print(f"Нельзя обучить команде животное {name}")
            return

    print(f"Животное с именем {name} не найдено")


def sort_animals_by_birth_date():
    animals_list.sort(key=lambda animal: animal.birth_date)

    print("Список животных отсортирован по дате рождения:")

    for animal in animals_list:
        print(f"Имя: {animal.name}, Дата рождения: {animal.birth_date}")


def print_total_animals_count():
    print(f"Общее количество животных: {len(animals_list)}")

