from menu import Menu, MenuItem
import commands

def create_main_menu():
    items = [
        MenuItem('1', 'New Game', commands.not_yet_implemented),
        MenuItem('2', 'Load Game', commands.not_yet_implemented),
        MenuItem('0', 'Exit', commands.exit)
        ]
    return Menu(items)
