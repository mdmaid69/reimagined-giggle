def is_palindrome(s):
        return s == s[::-1]
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))