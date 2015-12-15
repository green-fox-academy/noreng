import commands

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

    def select_item(self, choice):
        for item in self.items:
          if item.id == choice:
            return item.action()
        return commands.Result(success = False, text = '{} is wrong input'.format(choice))

    def display(self):
        while True:
            self.show()
            action = self.select_item(self.ask_player())
            if action.success == False:
                print(action.text)
            elif action.success == None:
                print('exit')
                break

    def ask_player(self):
        return input('Choose an option: ')
