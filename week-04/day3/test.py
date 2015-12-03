a = 40
b = 30
c = 20
value = 100

def test(n):
    globals()[a] = 3
    return globals()[a]

# def input(param1):
#    return value + 1
#
# value = input(3)

print(test(a))

print(a)
print(b)
print(c)
print(value)
