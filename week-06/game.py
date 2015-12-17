from actions import *
from random import randint
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

class Player:
    def __init__(self):
        self.name = ''
        self.stats = {'dexterity': 0, 'health': 0, 'luck': 0}
        self.stats_start = {}
        self.extra_potion = ''
        self.inventory = {'weapon': 'Magic Sword', 'armor': 'Supermagic', 'extra potion': self.extra_potion}

    def get_stats(self):
        return self.dictionary_to_string(self.stats)

    def get_inventory(self):
        return self.dictionary_to_string(self.inventory)

    def display_stats(self):
        print(self.get_stats() + '\n')

    def display_inventory(self):
        print(self.get_inventory() + '\n')

    def set_name(self):
        self.name = self.ask_player('What\'s your name? ')

    def get_name(self):
        return self.name

    def greet(self):
        return 'Hi ' + self.name + '!'

    def display_greet(self):
        print('\n' + self.greet() + '\n')

    def change_name(self):
        message = 'Change your current name ({}) to: '.format(self.name)
        self.name = self.ask_player(message)

    def ask_player(self, text):
        return input(text)

    def set_basic_stats(self):
        self.stats['dexterity'] = self.roll_dice() + 6
        self.stats['health'] = self.roll_dice() + self.roll_dice() + 12
        self.stats['luck'] = self.roll_dice() + 6
        self.set_max_stats()

    def set_max_stats(self):
        self.stats_start = self.stats

    def roll_dice(self):
        return randint(1,6)

    def set_extra_potion(self, potion):
        self.extra_potion = potion
        self.inventory['extra potion'] = potion

    def get_extra_potion(self):
        return self.extra_potion

    def use_extra_potion(self):
        self.stats[self.extra_potion] = self.stats_start[self.extra_potion]

    def dictionary_to_string(self, dict):
        items = dict.items()
        return ", ".join(str(key).capitalize() + ': ' + str(value) for key, value in items)
