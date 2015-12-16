import commands as cmd
from menu import *
import time

def main_menu(game):
    game.set_menu(menus.main)
    return cmd.Result(True)

def new_game(game):
    game.player.add_name()
    game.set_menu(menus.new_game)
    return cmd.Result(True)

def exit_from_game(game):
    game.exit = True

def reenter_name(game):
    game.player.change_name()
    return cmd.Result(True)

def roll_stats(game):
    game.player.set_basic_stats()
    game.set_menu(menus.roll_stats)
    game.player.display_stats()
    return cmd.Result(True)

def select_potion(game):
    game.set_menu(menus.potion_menu)
    return cmd.Result(True)

def selected_potion(game, potion):
    game.player.set_extra_potion(potion)
    print('Your chosen potion is: ' + str(game.player.extra_potion))
    game.set_menu(menus.choosed_potion)
    return cmd.Result(True)

def display_player_stats(game):
    print('Here is your character:')
    game.player.display_stats()
    game.player.display_inventory()
    game.set_menu(menus.begin)
    return cmd.Result(True)

class Menus:
    def main(self):
        return Menu([
            MenuItem('1', 'New Game', new_game),
            MenuItem('2', 'Load Game', cmd.Not_Implemented),
            MenuItem('0', 'Exit', exit_from_game)
            ])

    def new_game(self):
        return Menu([
            MenuItem('1', 'Reenter name', reenter_name),
            MenuItem('2', 'Continue -> Roll Stats', roll_stats),
            MenuItem('3', 'Save', cmd.Not_Implemented),
            MenuItem('4', 'Back to main menu', main_menu),
            MenuItem('0', 'Quit', cmd.Not_Implemented)
            ])

    def quit(self):
        return Menu([
            MenuItem('1', 'Save and Quit', cmd.Not_Implemented),
            MenuItem('2', 'Quit without Save', cmd.Not_Implemented),
            MenuItem('0', 'Resume', cmd.Not_Implemented),
            ])

    def roll_stats(self):
        return Menu([
            MenuItem('1', 'Reroll stats', roll_stats),
            MenuItem('2', 'Continue -> Select potion', select_potion),
            MenuItem('3', 'Save', cmd.Not_Implemented),
            MenuItem('0', 'Quit', cmd.Not_Implemented),
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
            MenuItem('0', 'Quit', cmd.Not_Implemented),
            ])

    def begin(self):
        return Menu([
            MenuItem('1', 'Begin', cmd.Not_Implemented),
            MenuItem('2', 'Save', cmd.Not_Implemented),
            MenuItem('0', 'Quit', cmd.Not_Implemented),
            ])

menus = Menus()
