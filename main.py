import collections
def create_stack():
        return collections.deque()
def is_palindrome(s):
        return s == s[::-1]