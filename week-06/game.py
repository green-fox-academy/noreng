from actions import *
from random import randint
import os

class Game:
    def __init__(self):
        self.action = None
        self.action_arg = None
        self.menu = None
        self.player = Player()
        self.continue_ = True

    def execute_action(self):
        if not self.action:
            self.action = main_menu
        return self.action(self)

    def set_next_action(self, action, arg = None):
        self.action = action
        self.action_arg = arg

    def get_action_arg(self):
        return self.action_arg

    def set_action_from_menu(self, text):
        choice = self.ask('\n' + text)
        self.menu.select_item(choice, self)

    def title(self, text):
        print('\n' + text + '\n')

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
        self.inventory = ['Sword', 'Leather Armor', self.extra_potion]

    def get_stats(self):
        return "\n".join(str(key) + ': ' + str(value) for key, value in self.stats.items())

    def get_inventory(self):
        return "\n".join(item for item in self.inventory)

    def display_stats(self):
        print(self.get_stats())

    def display_inventory(self):
        print(self.get_inventory())

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
        self.inventory[2] = potion

    def get_extra_potion(self):
        return self.extra_potion

    def use_extra_potion(self):
        self.stats[self.extra_potion] = self.stats_start[self.extra_potion]
