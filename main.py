import re
def split_string(pattern, string):
        return re.split(pattern, string)
def is_palindrome(s):
        return s == s[::-1]