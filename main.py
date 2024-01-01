import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def is_palindrome(s):
        return s == s[::-1]