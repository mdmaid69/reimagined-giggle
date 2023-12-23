def is_palindrome(s):
        return s == s[::-1]
import collections
def create_stack():
        return collections.deque()