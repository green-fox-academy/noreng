numbers = [1,2,3,5,6,7,120]

maximum = numbers[0]

for n in numbers:
    if maximum < n:
        maximum = n

print(maximum)  # 120
