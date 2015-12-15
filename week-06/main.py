from menu import MenuItem, Menu
from menuitems import create_main_menu

def main():
    menu = create_main_menu()

    while True:
        menu.pretty_print()
        choice = input("Choose an option: ")
        result = menu.select_item(choice)

        if result == 'exit':
            print('exit')
            break

main()
