from menu import *
import time

def not_implemented(game):
    game.set_message('Sorry, not yet implemented')
    return game.resume_action()

def show_main_menu(game):
    game.title('Welcome!')
    game.display_menu(menus.main)
    game.set_action_from_menu('Choose the next step: ')

def set_name(game):
    game.title('My name is Norbert')
    game.player.set_name()
    game.set_next_action(new_game)

def new_game(game):
    game.player.display_greet()
    game.display_menu(menus.new_game)
    game.set_action_from_menu('Choose an option: ')

def reenter_name(game):
    game.title('Reenter name')
    game.player.change_name()
    game.set_next_action(new_game)

def show_exit_menu(game):
    game.title('Do you really want to exit?')
    confirm = input('Press \'q\' to confirm: ')
    if confirm == 'q':
        return game.exit()
    game.set_message('Cancelled')
    return game.resume_action()

def exit_from_game(game):
    game.exit()

def resume(game):
    game.resume_action()

def roll_stats(game):
    game.title('Roll stats...')
    time.sleep(3)
    game.player.set_basic_stats()
    game.set_next_action(show_stats)

def show_stats(game):
    game.title('Here are your lucky stats:')
    game.player.display_stats()
    game.display_menu(menus.roll_stats)
    game.set_action_from_menu('Choose: ')

def select_potion(game):
    game.title('Select potion: ')
    game.display_menu(menus.potion_menu)
    game.set_action_from_menu('Choose wisely: ')

def selected_potion(game):
    potion = game.get_action_arg()
    game.player.set_extra_potion(potion)
    selected_potion = game.player.get_extra_potion()
    game.title('Your selected potion: {}'.format(selected_potion))
    game.display_menu(menus.choosed_potion)
    game.set_action_from_menu('You choosed wisely. Change option: ')

def display_player_stats(game):
    name = game.player.get_name()
    game.title('{}, here is your character:'.format(name))
    game.player.display_stats()
    game.player.display_inventory()
    game.display_menu(menus.begin)
    game.set_action_from_menu('Are you ready to start? ')

class Menus:
    def main(self):
        return Menu([
            MenuItem('1', 'New Game', set_name),
            MenuItem('2', '(Load Game)', not_implemented),
            MenuItem('0', 'Quit', show_exit_menu)
            ])

    def new_game(self):
        return Menu([
            MenuItem('1', 'Continue -> Roll Stats', roll_stats),
            MenuItem('2', 'Reenter name', reenter_name),
            MenuItem('3', '(Save)', not_implemented),
            MenuItem('4', 'Back to main menu', show_main_menu),
            MenuItem('0', 'Quit', show_exit_menu)
            ])

    def quit(self):
        return Menu([
            MenuItem('1', '(Save and Quit)', not_implemented),
            MenuItem('2', '(Quit without Save)', not_implemented),
            MenuItem('0', '(Resume)', not_implemented),
            ])

    def roll_stats(self):
        return Menu([
            MenuItem('1', 'Continue -> Select potion', select_potion),
            MenuItem('2', 'Reroll stats', roll_stats),
            MenuItem('0', 'Quit', show_exit_menu),
            ])

    def potion_menu(self):
        return Menu([
            MenuItem('1', 'Potion of Health', selected_potion, 'health'),
            MenuItem('2', 'Potion of Dexterity', selected_potion, 'dexterity'),
            MenuItem('3', 'Potion of Luck', selected_potion, 'luck'),
            ])

    def choosed_potion(self):
        return Menu([
            MenuItem('1', 'Continue -> Begin', display_player_stats),
            MenuItem('2', 'Reselect the Potion', select_potion),
            MenuItem('0', 'Quit', show_exit_menu),
            ])

    def begin(self):
        return Menu([
            MenuItem('1', '(Begin)', not_implemented),
            MenuItem('2', '(Save)', not_implemented),
            MenuItem('0', 'Quit', show_exit_menu),
            ])

    def save(self):
        return Menu([
            MenuItem('1', '(Add new item)', not_implemented),
            MenuItem('2', '(Resume)', not_implemented),
            MenuItem('0', 'Quit', show_exit_menu),
            ])

menus = Menus()
