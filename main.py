import re
print(re.match("h.*o", "hello world"))
def is_palindrome(s):
        return s == s[::-1]