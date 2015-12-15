from menu import *
import commands as cmd
import actions as ac

def menuitems():
    return {
    'main' : [
    MenuItem('1', 'New Game', ac.new_game),
    MenuItem('2', 'Load Game', cmd.Not_Implemented),
    MenuItem('0', 'Exit', cmd.Exit)
    ],
    'new_game' : [
    MenuItem('1', 'Reenter name', ac.reenter_name),
    MenuItem('2', 'Continue', cmd.Not_Implemented),
    MenuItem('3', 'Save', cmd.Not_Implemented),
    MenuItem('0', 'Quit', cmd.Not_Implemented)
    ]
    }

def create_menu(items):
    return Menu(items)
