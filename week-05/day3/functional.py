def adder(array):
    return list(map(lambda x: x + 1, array))

def adder_with_for(array):
    new_array = []
    for number in array:
        new_array.append(number + 1)
    return new_array

def adder_with_map(array):
    def add1(n):
        return n + 1
    return list(map(add1, array))



def filter_array(array):
    return list(filter(lambda x: x % 3 == 0, array))

def filter_array_with_list_compr(array):
    return [x for x in array if x % 3 == 0]
