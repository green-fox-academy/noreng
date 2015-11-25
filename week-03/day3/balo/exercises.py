# 1 create MySuperString class
# 2 Receive a string as an arg and store it
# 3 Implement reverse()
#       'hello' => 'olleh'
# 4 implement count(char)
# 5 implement snake_case()
# 6 create myMath class
#   6.1 create a method in the class that returns the avg of the numbers

class MySuperString:
    def __init__(self, mystr):
        self.mystr = mystr

    # reverse: my solution with while
    def myReverse(self):
        i = 0
        newString = ""
        while i < len(self.mystr):
            newString = self.mystr[i] + newString
            i += 1
        return newString

    # reverse: with range
    def reverse(self):
        n = len(self.mystr)
        reversed = ''
        for i in range(n):
            reversed = self.mystr[i] + reversed
        return reversed

    # reverse: with range2
    def reverse2(self):
        n = len(self.mystr)
        reversed = ''
        for i in range(n-1, -1, -1):
            reversed += self.mystr[i]
        return reversed

    # reverse: shorter solution
    def reverse3(self):
        reversed = ''
        for i in self.mystr:
            reversed = i + reversed
        return reversed

    # counter
    def countCharacter(self, letter):
        counter = 0
        for i in self.mystr:
            if i == letter:
                counter += 1
        return counter

    # snake_case()
    def snake_case(self):
        newString = ''
        for i in self.mystr:
            if i == ' ':
                newString += '_'
            else:
                newString += i.lower()
        return newString

    # camelCase()
    def camelCase(self):
        original = self.mystr
        newString = ''
        i = 0
        while i < len(original):
            before = original[i-1]
            current = original[i]
            if before == ' ' or before == '_':
                newString += current.upper()
            elif current == ' ' or current == '_':
                newString += ''
            else:
                newString += current.lower()
            i += 1
        return newString

class MyMath:
    def __init__(self):
        self

    def sum(self, num_list):
        total = 0
        for i in num_list:
            total += i
        return total

    def average(self, num_list):
        return sum(num_list) / len(num_list)
