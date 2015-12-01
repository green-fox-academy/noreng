my_file = open("text/duplicated_chars.txt")


text = my_file.read()
my_file.close()

# print the \n as well
print(repr(text))

def remove_duplicated_characters(txt):
    newText = ''
    i = 0
    while i < (len(txt)-1):
        if txt[i] == '\n':
            newText += '\n'
            i += 1
        elif txt[i:i+4] == txt[i] * 4:
            newText += txt[i] * 2
            i += 4
        elif txt[i] == txt[i+1]:
            newText += txt[i]
            i += 2
        else:
            newText += txt[i]
            i += 1
    return newText

print(remove_duplicated_characters(text))
