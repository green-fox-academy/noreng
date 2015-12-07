import re

def filereader():
    with open("test.txt", "r") as input:
        text = input.read()
        changed = re.sub(r'alma', '....', text)
        print(changed)

filereader()
