import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def is_palindrome(s):
        return s == s[::-1]