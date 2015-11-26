def reverse(in_list):
    reversed = []
    i = 1
    while i <= len(in_list):
        reversed.append(in_list[-i])
        i += 1
    return reversed

print(reverse([1,2,3,4]))
