import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def is_palindrome(s):
        return s == s[::-1]