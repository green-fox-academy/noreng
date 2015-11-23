number=0
while number < 100:
    n = str(number)
    if '3' in n or '5' in n:
        if ('3' in n) == False:
            print('buzz')
        elif ('5' in n) == False:
            print('fizz')
        else:
            print('fizzbuzz')
    else:
        print(n)
    number += 1
