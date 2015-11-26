def convertToList(string):
    stringList = string.split(',')
    return stringList

def isConsecutive(list):
    i = 1
    while i < len(list):
        currentNumber = int(list[i])
        prevNumber = int(list[i-1])
        if abs(currentNumber - prevNumber) != 1:
            return False
        i += 1
    return True

def isContainingNumbers(list):
    try:
        for i in list:
            int(i)
        return True
    except ValueError:
        return False

def multiplyItemsInList(list):
    multiplicated = 1
    for i in list:
        multiplicated *= int(i)
    return multiplicated

def alwaysPerfect(string):
    list = convertToList(string)

    if len(list) != 4:
        return 'incorrect input'
    elif isContainingNumbers(list) == False:
        return 'incorrect input'
    elif isConsecutive(list) == False:
        return 'not consecutive'

    perfectNumber = multiplyItemsInList(list) + 1
    root = int(perfectNumber ** 0.5)
    return str(perfectNumber) + ', ' + str(root)
