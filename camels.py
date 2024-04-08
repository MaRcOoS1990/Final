from datetime import datetime

class PackAnimals:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")

class Camels(PackAnimals):
    pass
