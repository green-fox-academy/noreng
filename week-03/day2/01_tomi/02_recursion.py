def f(n):
    if n == 0:
        return
    print("Hello")
    f (n-1)

f(5) # HelloHelloHelloHelloHello

# factorial
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5)) #120

# fibonacci
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(0)) # 0
print(fibo(1)) # 1
print(fibo(2)) # 1
print(fibo(3)) # 2
print(fibo(4)) # 3
print(fibo(5)) # 5
