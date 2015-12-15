from menuitems import Menus

class Game:
    def __init__(self):
        self.player = Player()
        self.current_menu = Menus().main()
        self.previous_menu = None

    def display_current_menu(self):
        self.current_menu.show()

    def set_next_menu(self, next_menu):
        self.current_menu = next_menu

class Player:
    def __init__(self):
        self.name = None

    def add_name(self):
        self.name = self.ask_player('Tell me your name: ')
        self.display_name()

    def change_name(self):
        message = 'Change your current name ({}) to: '.format(self.name)
        self.name = self.ask_player(message)
        self.display_name()

    def ask_player(self, text):
        return input(text)

    def display_name(self):
        print('Hi ' + self.name + '!')
