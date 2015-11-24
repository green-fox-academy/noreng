# greet
def greet(name):
    print("Hi " + name)

greet('Tojas') # 'Hi Tojas'

# add
def add(a, b):
    return a + b

print(add(3,4)) # 7

# number is even
def is_even(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(is_even(2)) # even
