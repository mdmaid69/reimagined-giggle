def is_palindrome(s):
        return s == s[::-1]
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))