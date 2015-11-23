number = 3049
divider = 2

# negative
if number < 0:
    print('negative number')
# zero
elif number == 0:
    print('zero')
# one
elif number == 1:
    print('one')
# even numbers
elif number % 2 == 0:
    # number is 2 -> prime
    if number == 2:
        print(str(number) +' | two, prime')
    # number is even -> not prime
    else:
        print(str(number) + ' | even, not prime')

else:
    # examining dividers < sqrt(number)
    while divider < number**0.5:
        if number % divider == 0:
            print(str(number) + ' | not prime')
            break
        else:
            divider += 1
    else:
        print(str(number) + ' | prime')
