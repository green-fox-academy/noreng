from menu import *
import commands as cmd
import actions as ac

class Menus:
    def main(self):
        return Menu([
            MenuItem('1', 'New Game', ac.new_game),
            MenuItem('2', 'Load Game', cmd.Not_Implemented),
            MenuItem('0', 'Exit', ac.exit_from_game)
            ])

    def new_game(self):
        return Menu([
            MenuItem('1', 'Reenter name', ac.reenter_name),
            MenuItem('2', 'Continue', cmd.Not_Implemented),
            MenuItem('3', 'Save', cmd.Not_Implemented),
            MenuItem('4', 'Back to main menu', ac.main_menu),
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
