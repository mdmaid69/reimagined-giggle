import collections
def create_queue():
        return collections.deque()
def is_palindrome(s):
        return s == s[::-1]