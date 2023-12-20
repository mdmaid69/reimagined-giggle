def is_palindrome(s):
        return s == s[::-1]
def find_unique_words(sentence):
        return set(sentence.split())