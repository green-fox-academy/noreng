import commands

class MenuItem:
    def __init__(self, id, text, command = None):
        self.id = id
        self.text = text
        self.command = command

    def __repr__(self):
        return '{} {}'.format(self.id, self.text)

class Menu:
    def __init__(self, items):
        self.items = items

    def pretty_print(self):
        print(self.get_menu())

    def get_menu(self):
        return "\n".join(str(item) for item in self.items)

    def select_item(self, choice):
        for item in self.items:
          if item.id == choice:
            return item.command
        return commands.Result(success = False, text = 'Wrong input')
