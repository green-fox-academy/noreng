from actions import *
from player import *
import os

class Game:
    def __init__(self):
        self.action = None
        self.action_arg = None
        self.prev_action = None
        self.menu = None
        self.player = Player()
        self.continue_ = True
        self.error = None
        self.message = None

    def execute_action(self):
        self.message = None
        self.error = None
        if not self.action:
            self.action = show_main_menu
        return self.action(self)

    def set_next_action(self, action, arg = None):
        self.action = action
        self.action_arg = arg

    def set_action_from_menu(self, text):
        choice = self.ask('\n' + text)
        self.menu.select_item(choice, self)

    def resume_action(self):
        self.action = self.prev_action

    def get_action_arg(self):
        return self.action_arg

    def title(self, text):
        print('\n' + text + '\n')

    def set_error(self, message):
        self.error = message

    def set_message(self, message):
        self.message = message

    def display_errors_and_messages(self):
        print("// Error: {}".format(self.error)) if self.error else None
        print("// {}".format(self.message)) if self.message else None

    def clear_display(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def display_menu(self, menu):
        self.menu = menu()
        self.menu.display()

    def ask(self, text):
        return input(text)

    def exit(self):
        self.continue_ = False
