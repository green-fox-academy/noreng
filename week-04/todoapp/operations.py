from item import Task

def read_db(path):
    db = open(path, "r")
    raw_content = db.read()
    db.close()
    database = raw_text_to_list(raw_content)
    database = [convert_to_object(row) for row in database]
    return database

def save_to_db(database, path):
    db = open(path, "w")
    raw_content = list_to_raw_text(database)
    db.write(raw_content)
    db.close()

def show_menu():
    print('\nMENU\n1 = add new task\n2 = complete task\n3 = remove task\n\n0 = exit\n')

def add_task(database):
    while True:
        pretty_print(database)
        userInput = input('\nNew task to do:\n')
        if userInput == '':
            break
        database.append(Task(userInput))

def remove_task(database):
    while True:
        pretty_print(database)
        userInput = input('\nNumber of task to delete:\n')
        try:
            if userInput == '':
                break
            i = int(userInput) - 1
            del database[i]
        except ValueError:
            print('Number, please')
        except IndexError:
            print('Wrong number')

def complete_task(database):
    while True:
        pretty_print(database)
        userInput = input('\nNumber of completed task:\n')
        try:
            if userInput == '':
                break
            i = int(userInput) - 1
            database[i].set_completed(True)
        except ValueError:
            print('Number, please')
        except IndexError:
            print('Wrong number')

def raw_text_to_list(text):
    list_ = text.split('\n')
    return [string for string in list_ if string != '']

def list_to_raw_text(list_):
    return "\n".join(str(i) for i in list_)

def convert_to_object(text):
    status = text[:3]
    description = text[4:]

    if status == '[x]':
        status = True
    else:
        status = False
    return Task(description, status)

def pretty_print(list_):
    print('\nTO DO LIST\n')
    if len(list_) == 0:
        print('\n-- Nothing to do --\n')

    pretty_list = []
    i = 0
    for task in list_:
        i += 1
        pretty_list.append(str(i) + '.\t' + str(task))
    print(("\n".join(str(i) for i in pretty_list)).expandtabs(2))
