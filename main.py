import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def is_palindrome(s):
        return s == s[::-1]