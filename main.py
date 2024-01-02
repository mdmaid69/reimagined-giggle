import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def is_palindrome(s):
        return s == s[::-1]