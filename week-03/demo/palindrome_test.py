from palindrome import *

def test(tested, expected):
    if tested == expected:
        print('Passed')
    else:
        print('Failed')

test(create_palindrome('pear'), 'pearraep')

test(is_palindrome('goog'), True)
test(is_palindrome('google'), False)

test(split_to_words('dog goat dad duck doodle never'), ['dog', 'goat', 'dad', 'duck', 'doodle', 'never'])

test(substring_variations('google'), ['goo', 'goog', 'googl', 'google', 'oog', 'oogl', 'oogle', 'ogl', 'ogle', 'gle'])

test(remove_duplicates(['ala', 'ala', 'olle']), ['olle','ala'])

test(filter_palindromes(['olle', 'ala']), ['ala'])

test(search_palindromes('dog goat dad duck doodle never'), ['dad', 'dood', 'eve'])

print(search_palindromes('dog goat dad duck doodle never'))
print(search_palindromes('dog goat a Dad duck doodle never'))
print(search_palindromes('dog goat a Dad duck doodle never'))
print(search_palindromes('dog'))
print(search_palindromes('a'))
print(search_palindromes(''))
