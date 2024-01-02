def is_palindrome(s):
        return s == s[::-1]
import re
def split_string(pattern, string):
        return re.split(pattern, string)