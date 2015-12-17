import commands as cmd
from menu import *
import time

def main_menu(game):
    game.title('Welcome!')
    game.display_menu(menus.main)
    game.set_action_from_menu('Choose the next step: ')

def set_name(game):
    game.title('My name is Norbert')
    game.player.add_name()
    game.set_next_action(new_game)

def new_game(game):
    game.player.display_greet()
    game.display_menu(menus.new_game)
    game.set_action_from_menu('Choose an option: ')

def exit_menu(game):
    game.title('Doy you really want to exit?')
    game.display_menu(menus.exit)
    game.set_action_from_menu('Choose an option: ')

def exit_from_game(game):
    game.exit()

def reenter_name(game):
    game.title('Reenter name')
    game.player.change_name()
    game.clear_display()
    game.player.display_greet()
    game.display_menu(menus.new_game)
    game.set_action_from_menu('Choose from the options above: ')

def roll_stats(game):
    game.title('Roll stats...')
    time.sleep(3)
    game.set_next_action(show_stats)

def show_stats(game):
    game.title('Here are your lucky stats:')
    game.player.set_basic_stats()
    game.player.display_stats()
    game.display_menu(menus.roll_stats)
    game.set_action_from_menu('Choose: ')

def select_potion(game):
    game.title('Select potion: ')
    game.display_menu(menus.potion_menu)
    game.set_action_from_menu('Choose wisely: ')

class Menus:
    def main(self):
        return Menu([
            MenuItem('1', 'New Game', set_name),
            MenuItem('2', '(Load Game)', cmd.Not_Implemented),
            MenuItem('0', 'Exit', exit_menu)
            ])

    def new_game(self):
        return Menu([
            MenuItem('1', 'Continue -> Roll Stats', roll_stats),
            MenuItem('2', 'Reenter name', reenter_name),
            MenuItem('3', '(Save)', cmd.Not_Implemented),
            MenuItem('4', 'Back to main menu', main_menu),
            MenuItem('0', 'Quit', exit_menu)
            ])

    def exit(self):
        return Menu([
            MenuItem('0', 'Yes', exit_from_game),
            MenuItem('1', 'No*', main_menu),
            ])

    def quit(self):
        return Menu([
            MenuItem('1', '(Save and Quit)', cmd.Not_Implemented),
            MenuItem('2', '(Quit without Save)', cmd.Not_Implemented),
            MenuItem('0', '(Resume)', cmd.Not_Implemented),
            ])

    def roll_stats(self):
        return Menu([
            MenuItem('1', 'Continue -> Select potion', select_potion),
            MenuItem('2', 'Reroll stats', roll_stats),
            MenuItem('0', '(Quit)', exit_menu),
            ])

    def potion_menu(self):
        return Menu([
            MenuItem('1', 'Potion of Health', selected_potion, 'health'),
            MenuItem('2', 'Potion of Dexterity', selected_potion, 'dexterity'),
            MenuItem('3', 'Potion of Luck', selected_potion, 'luck'),
            ])

    def choosed_potion(self):
        return Menu([
            MenuItem('1', 'Reselect the Potion', select_potion),
            MenuItem('2', 'Continue -> Begin', display_player_stats),
            MenuItem('0', '(Quit)', exit_menu),
            ])

    def begin(self):
        return Menu([
            MenuItem('1', '(Begin)', cmd.Not_Implemented),
            MenuItem('2', '(Save)', cmd.Not_Implemented),
            MenuItem('0', '(Quit)', exit_menu),
            ])

    def save(self):
        return Menu([
            MenuItem('1', '(Add new item)', cmd.Not_Implemented),
            MenuItem('2', '(Resume)', cmd.Not_Implemented),
            MenuItem('0', '(Quit)', exit_menu),
            ])

menus = Menus()
