def greet(name):
    return "Hello, " + name

result = greet("Tomi")
print(result)

g=[]

def add(a, b):
    res = a + b
    g.append(res)
    return res

print(add(1, 2))
print(add(7, 2))
print(add(0.1, 2))
print(g)

# scoping
n = 1

def my_print():
    n = 2
    print(n)

my_print() #2
print(n) #1

# greetByWord
def greetByWord(name, hi = None):
    if hi is None:
        hi = "Hello"
    return hi + ", " + name

hi = greetByWord("Norbi", "Haliho")
print(hi)
hi = greetByWord("Norbi", "Haliho")
print(hi)

#default parameter is a global value!
def add2(a, b, res = []): # this way we can add 2 or 3 args
    r = a + b
    res.append(r)
    print(res)
    return r

add2(1,2) # [3]
add2(2,3) # [3, 5]
add2(4,5) # [3, 5, 9]


def add3(a, b, res = None): # this way we can add 2 or 3 args
    if res is None:
        res = []
    r = a + b
    res.append(r)
    print(res)
    return r

add3(1,2) # [3]
add3(2,3) # [5]
add3(4,5) # [9]
