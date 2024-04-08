from datetime import datetime

import app


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

class Dogs(Pets):
    pass

class Cats(Pets):
    pass


dog = Dogs("Борис", "01.01.2013", ["Сидеть", "Лежать"])
cat = Cats("Мура", "01.02.2016", ["Присесть", "Крутиться"])



print(f"Имя собаки: {dog.name}")
print(f"Дата рождения собаки: {dog.birth_date}")
print(f"Команды собаки: {dog.get_commands()}")

print(f"Имя кошки: {cat.name}")
print(f"Дата рождения кошки: {cat.birth_date}")
print(f"Команды кошки: {cat.get_commands()}")

# if __name__ == '__main__':
    # app.main()
