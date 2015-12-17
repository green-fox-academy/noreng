from game import Game
import os

def main():
    game = Game()

    while game.continue_:
        game.clear_display()
        game.execute_action()

    print('Goodbye!')

main()
