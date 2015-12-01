in_file = open("text/encoded_zen_lines.txt", "r")
out_file = open("out/decoded_zen_lines.txt", "w")

original = in_file.readlines()

def encodeCharacter(character, offset = 1):
    return chr(ord(character) + offset)

def encodeString(string, offset = 0):
    encoded = ''
    for char in string:
        if char == ' ':
            encoded += ' '
        else:
            encoded += encodeCharacter(char, offset )
    return encoded

for line in original:
    out_file.write(encodeString(line, -1) + '\n')

in_file.close()
out_file.close()

print('ready')
