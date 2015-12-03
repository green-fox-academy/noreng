from operations import *

def main():
    # read
    database = read_db('database/database.txt')
    print_todo_list(database)

    # while
    while True:
        # menu print
        show_menu()
        # input from user
        user_input = int(input('Choose one: '))

        # execute
        if user_input == 1:
            add_task(database)
        elif user_input == 2:
            complete_task(database)
        elif user_input == 3:
            remove_task(database)
        elif user_input == 0:
            # if "save" - > break, save
            break

    # save_to_file
    save_to_db(database, 'database/database.txt')
    print('Saved')

main()
