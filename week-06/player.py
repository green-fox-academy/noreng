from random import randint

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
