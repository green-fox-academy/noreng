from menu import Menu, MenuItem
import commands

def create_main_menu():
    items = [
        MenuItem('1', 'New Game', commands.Result(None)),
        MenuItem('2', 'Load Game', commands.Result(None)),
        MenuItem('0', 'Exit', 'exit')
        ]
    return Menu(items)
