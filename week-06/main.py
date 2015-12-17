from game import Game

def main():
    game = Game()
    while game.continue_:
        game.clear_display()
        game.display_errors_and_messages()
        game.execute_action()
    print('Goodbye!')

main()
