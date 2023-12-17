def is_palindrome(s):
        return s == s[::-1]
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))