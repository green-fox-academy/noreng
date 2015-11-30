# 1 duplicate() function
af = 123

def duplicate(n):
    return n * 2

print(duplicate(af))
# > 246


# 2 appendA() function
ag = 'kuty'

def appendA(string):
    return string + 'a'

print(appendA(ag))
# > kutya


# 3 reuse appendA() function in list
ag2 = ['rep', 'macsk', 'cic', 'Ann']

for i in range(len(ag2)):
    ag2[i] = appendA(ag2[i])

print(ag2)


# 4 sumlist() function
numbers = [4, 5, 6, 7, 8, 9]

def sumlist(list_):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(sumlist(numbers))


# 5 factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
