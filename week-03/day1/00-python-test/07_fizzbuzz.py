n=0
while n < 100:
    if n % 3 == 0 or n % 5 == 0:
        if n % 3 != 0:
            print('buzz')
        elif n % 5 != 0:
            print('fizz')
        else:
            print('fizzbuzz')
    else:
        print (n)
    n += 1
