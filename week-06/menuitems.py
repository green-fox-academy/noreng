from menu import *
import commands as cmd

menuitems = {
        'main' : [
        MenuItem('1', 'New Game', cmd.Not_Implemented),
        MenuItem('2', 'Load Game', cmd.Not_Implemented),
        MenuItem('0', 'Exit', cmd.Exit)
        ],
        'new_game' : [
        MenuItem('1', 'Reenter name', cmd.Not_Implemented),
        MenuItem('2', 'Continue', cmd.Not_Implemented),
        MenuItem('3', 'Save', cmd.Not_Implemented),
        MenuItem('0', 'Quit', cmd.Exit)
        ]
        }

def create_menu(items):
    return Menu(items)
