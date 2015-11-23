number = 15
a, b = 0, 1
fibonacci = []

i = 0
while i < number:
    fibonacci.append(a)
    a,b = b, a+b
    i+=1

print(fibonacci)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
