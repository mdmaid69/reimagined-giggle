text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)