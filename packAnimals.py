from datetime import datetime

class Animals:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")

class PackAnimals(Animals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
