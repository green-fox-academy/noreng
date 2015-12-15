import commands as cmd

class MenuItem:
    def __init__(self, id, text, action = None):
        self.id = id
        self.text = text
        self.action = action

    def __repr__(self):
        return '{} {}'.format(self.id, self.text)

class Menu:
    def __init__(self, items):
        self.items = items

    def show(self):
        print(self.get_menu())

    def get_menu(self):
        return "\n".join(str(item) for item in self.items)

    def select_item(self, choice, store):
        for item in self.items:
          if item.id == choice:
            return item.action(store)
        return cmd.Result(success = False, text = '{} is wrong input'.format(choice))

    def ask_player(self):
        return input('Choose an option: ')
