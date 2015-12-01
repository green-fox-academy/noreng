# to import folder/reverse.py file:
from folder.reverse import reverse_list
# to import folder/subfolder/example.py file:
# from {folder..example} import {function_name}

print(reverse_list([1,2,3,4,5]))
# > [5, 4, 3, 2, 1]


# os module provides operating system dependent functionality:
import os

print(os.getpid())
# returns the current process’s id.


# open file
alma_file = open('alma.txt')
print(alma_file.read())
alma_file.close()
