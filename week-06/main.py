from menu import MenuItem, Menu, menu_items

def main():
    menu = menu_items()

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
