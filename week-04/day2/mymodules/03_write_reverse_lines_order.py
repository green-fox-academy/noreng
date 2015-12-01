in_file = open("text/zen_of_python.txt", "r")
out_file = open("out/reversed_zen_order.txt", "w")

original = in_file.readlines()

def reverse_lines_order(lst):
    return lst[::-1]

for line in reverse_lines_order(original):
    out_file.write(line)

in_file.close()
out_file.close()

print('ready')
