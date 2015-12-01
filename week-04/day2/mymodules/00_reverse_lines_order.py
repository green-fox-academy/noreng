my_file = open("text/reversed_zen_order.txt")



# read full text
text = my_file.read()
my_file.close()

def reverse_line_order_from_text(text):
    lines = text.split('\n')
    return '\n'.join(lines[::-1])

print(reverse_line_order_from_text(text))
print('\n')



# read all lines
my_file2 = open("text/reversed_zen_order.txt")
my_lines = my_file2.readlines()
my_file2.close()

def reverse_line_order_from_list(list):
    return ''.join(list[::-1])

print(reverse_line_order_from_list(my_lines))
