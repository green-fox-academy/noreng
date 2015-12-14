from menu import MenuItem, Menu, create_main_menu

def main():
    menu = create_main_menu()

    while True:
        menu.pretty_print()
        choice = input("Choose an option: ")
        result = menu.select_item(choice)

        if result == 'exit':
            print('exit')
            break

        elif result.success == False:
            print(result.text)

main()
