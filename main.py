import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def is_palindrome(s):
        return s == s[::-1]