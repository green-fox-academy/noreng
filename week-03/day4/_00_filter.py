numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# solution 'for'
def filter_even(list):
    resultList = []
    for n in list:
        if n % 2 == 0:
            resultList.append(n)
    return resultList

print(filter_even(numbers))

# solution 'while'
numbers2 = [10, 11, 12, 13, 14, 15, 16]
output = []
i = 0
while i < len(numbers2):
    if numbers2[i] % 2 == 0:
        output.append(numbers2[i])
    i += 1

print(output)
