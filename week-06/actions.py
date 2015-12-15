from menuitems import Menus
import commands as cmd

def main_menu(game):
    game.set_next_menu(Menus().main())
    return cmd.Result(True)

def new_game(game):
    game.player.add_name()
    game.set_next_menu(Menus().new_game())
    return cmd.Result(True)

def exit_from_game(game):
    return cmd.Result('Exit')

def reenter_name(game):
    game.player.change_name()
    return cmd.Result(True)
