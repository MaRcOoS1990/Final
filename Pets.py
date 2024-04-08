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

    # We can keep the setCommands method unimplemented for now 
    # by raising a NotImplementedError exception 
    def set_commands(self, new_commands):
        raise NotImplementedError("Setting commands not currently supported")
