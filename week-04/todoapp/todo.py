from operations import *

def main():
    database = read_db('database/database.txt')
    print_todo_list(database)

    while True:
        show_menu()
        user_input = int(input('Choose one: '))

        if user_input == 1:
            add_task(database)
        elif user_input == 2:
            complete_task(database)
        elif user_input == 3:
            remove_task(database)
        elif user_input == 0:
            break

    save_to_db(database, 'database/database.txt')
    print('Saved')

main()
