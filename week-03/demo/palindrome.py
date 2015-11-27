def create_palindrome(word):
    return word + word[::-1]

def is_palindrome(word):
    return word == word[::-1]

def split_to_words(sentence):
    return sentence.split()

def substring_variations(word):
    substrings = []
    wordLength = len(word)
    for i in range(wordLength - 2):
        for j in range(i + 3, wordLength + 1):
            substrings.append(word[i:j])
    return substrings

def remove_duplicates(list_):
    return list(set(list_))

def filter_palindromes(list_):
    palindromes = []
    for word in list_:
        if is_palindrome(word):
            palindromes.append(word)
    return palindromes

def search_palindromes(sentence):
    palindromes_found = []
    words = split_to_words(sentence)
    for word in words:
        substrings = substring_variations(word)
        unique_substrings = remove_duplicates(substrings)
        palindromes = filter_palindromes(unique_substrings)
        palindromes_found.extend(palindromes)
    return palindromes_found
