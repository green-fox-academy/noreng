from actions import *
from random import randint
import time

class Game:
    def __init__(self):
        self.player = Player()
        self.current_menu = Menus().main()
        self.exit = False

    def set_menu(self, next_menu):
        self.current_menu = next_menu()

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

    def add_name(self):
        self.name = self.ask_player('What\'s your name? ')
        self.display_greet()

    def greet(self):
        return 'Hi ' + self.name + '!'

    def display_greet(self):
        print(self.greet())

    def change_name(self):
        message = 'Change your current name ({}) to: '.format(self.name)
        self.name = self.ask_player(message)
        self.display_greet()

    def ask_player(self, text):
        return input(text)

    def set_basic_stats(self):
        print('Rolling...')
        time.sleep(0.5)
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

    def use_extra_potion(self):
        self.stats[self.extra_potion] = self.stats_start[self.extra_potion]
