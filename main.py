def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def is_palindrome(s):
        return s == s[::-1]