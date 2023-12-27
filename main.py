def is_palindrome(s):
        return s == s[::-1]
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)