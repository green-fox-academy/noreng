from exercises import MySuperString, MyMath

imported = dir(MySuperString)
print(imported)


test = MySuperString('HeLLo grEEnfox')
print(test.mystr)
print(test.reverse())
print(test.countCharacter('E'))
print(test.snake_case())
print(test.camelCase())


test2 = MyMath()
print(test2.average([1,2,3,4,7]))
print(test2.sum([1,2,3,4,7]))
