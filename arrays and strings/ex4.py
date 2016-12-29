from collections import Counter

def is_palindrome_permutation(input_str):
    input_str = input_str.replace(' ', '')
    counter = Counter(input_str)
    odd_words_count = len([x for x in counter if counter[x]%2 == 1])
    return odd_words_count < 2