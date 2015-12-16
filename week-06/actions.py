import commands as cmd
from menu import *

def main_menu(game):
    game.set_next_menu(menus.main)
    return cmd.Result(True)

def new_game(game):
    game.player.add_name()
    game.set_next_menu(menus.new_game)
    return cmd.Result(True)

def exit_from_game(game):
    return cmd.Result('Exit')

def reenter_name(game):
    game.player.change_name()
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
            MenuItem('2', 'Continue', cmd.Not_Implemented),
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
            MenuItem('1', 'Reroll stats', cmd.Not_Implemented),
            MenuItem('2', 'Continue', cmd.Not_Implemented),
            MenuItem('3', 'Save', cmd.Not_Implemented),
            MenuItem('0', 'Quit', cmd.Not_Implemented),
            ])

    def potion_menu(self):
        return Menu([
            MenuItem('1', 'Potion of Health', cmd.Not_Implemented),
            MenuItem('2', 'Potion of Dexterity', cmd.Not_Implemented),
            MenuItem('3', 'Potion of Luck', cmd.Not_Implemented),
            ])

    def choosed_potion(self):
        return Menu([
            MenuItem('1', 'Reselect the Potion', cmd.Not_Implemented),
            MenuItem('2', 'Continue', cmd.Not_Implemented),
            MenuItem('0', 'Potion of Luck', cmd.Not_Implemented),
            ])

    def begin(self):
        return Menu([
            MenuItem('1', 'Begin', cmd.Not_Implemented),
            MenuItem('2', 'Save', cmd.Not_Implemented),
            MenuItem('0', 'Quit', cmd.Not_Implemented),
            ])

menus = Menus()
