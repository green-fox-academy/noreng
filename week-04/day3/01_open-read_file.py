# my_file = open("alma.txt", "r")

def wc(fileName):
    input_file = open(fileName, "r")
    content = input_file.read()
    line_count = len(content.split('\n'))
    input_file.close()
    return [line_count, len(content)]

print(wc('alma.txt'))
