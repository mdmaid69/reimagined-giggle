def is_palindrome(s):
        return s == s[::-1]
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)