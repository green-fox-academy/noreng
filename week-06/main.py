from game import Game

def main():
    game = Game()

    while True:
        menu = game.current_menu
        menu.display()

        choice = menu.ask_player()
        action = menu.select_item(choice, game)

        if game.exit:
            print('Goodbye!')
            break

        if action.success == False:
            print(action.text)

main()
