my_file = open('text/reversed_zen_lines.txt')

my_lines = my_file.readlines()
my_file.close()

def reverse_lines(lst):
    return ''.join([x[::-1] for x in lst])

print(reverse_lines(my_lines))
