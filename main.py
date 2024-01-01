import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def is_palindrome(s):
        return s == s[::-1]