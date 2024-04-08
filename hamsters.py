from datetime import datetime

class Pets:
    def __init__(self, name, birth_date, commands):
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
        self.commands = commands

class Hamsters(Pets):
    pass
