from item import Task

def read_db(path):
    db = open(path, "r")
    raw_content = db.read()
    db.close()
    database = raw_text_to_list(raw_content)
    return database

def save_to_db(database, path):
    db = open(path, "w")
    raw_content = list_to_raw_text(database)
    db.write(raw_content)
    db.close()

def show_menu():
    print('\nMENU\n')
    print('1 = add new task\n2 = complete task\n3 = remove task\n\n0 = exit\n')

def add_task(database):
    while True:
        userInput = input('\nNew task to do:\n')
        if userInput == '':
            break
        database.append(Task(userInput))
        print(database)
        print_todo_list(database)

def remove_task(database):
    while True:
        print_todo_list(database)
        userInput = input('\nNumber of task to delete:\n')
        if userInput == '':
            break
        i = int(userInput) - 1
        del database[i]

def complete_task(database):
    while True:
        print_todo_list(database)
        userInput = input('\nNumber of completed task:\n')
        if userInput == '':
            break
        i = int(userInput) - 1
        database[i].set_completed(True)

def raw_text_to_list(text):
    list_ = text.split('\n')
    return [string for string in list_ if string != '']

def list_to_raw_text(list_):
    return "\n".join(str(i) for i in list_)

def print_todo_list(list_):
    print('\nTO DO LIST\n')
    nasd = []
    i = 0
    for item in list_:
        i += 1
        nasd.append(str(i) + '. ' + str(item))
    print("\n".join(str(i) for i in nasd))
