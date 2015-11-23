n=0
while n < 100:
    if n % 3 == 0:
        if n % 5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)
    n += 1
