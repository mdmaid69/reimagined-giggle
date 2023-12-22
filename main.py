import array
def get_array_as_frozenset(array):
        return frozenset(array)
def is_palindrome(s):
        return s == s[::-1]