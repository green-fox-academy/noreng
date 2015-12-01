def reverse_list(lst):
    reversed = []
    i = len(lst) - 1
    while i >= 0:
        reversed.append(lst[i])
        i -=1
    return reversed
