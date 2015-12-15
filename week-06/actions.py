# from menu import *
from menuitems import create_menu, menuitems
from player import *

def main_menu():
    menu = create_menu(menuitems()['main'])
    menu.display()

def new_game():
    player = Player()
    player.ask_player_name()
    player.display_name()
    menu = create_menu(menuitems()['new_game'])
    menu.display()

def reenter_name():
    player = Player()
    player.ask_player_name()
    player.display_name()
    menu = create_menu(menuitems()['new_game'])
    menu.display()
