from always_perfect import *

def test(tested, expected):
    if tested == expected:
        print('Passed')
    else:
        print('Failed')

test(convertToList('4,5,6,7'), ['4','5','6','7'])

test(isConsecutive([2, 3, 4, 5, 6]), True)
test(isConsecutive([6, 5, 4, 3, 2]), True)
test(isConsecutive([9, 10, 11, 13]), False)

test(isContainingNumbers(['4','5','6','7']), True)
test(isContainingNumbers(['4','5','a','7']), False)

test(multiplyItemsInList(['1','2','3','4']), 24)

test(alwaysPerfect('4, 5, 6, 7'), '841, 29')
test(alwaysPerfect('8, 7, 6, 5'), '1681, 41')
test(alwaysPerfect('4, 5, 6, 8, 9'), 'incorrect input')
test(alwaysPerfect('4, 5, x, 8'), 'incorrect input')
