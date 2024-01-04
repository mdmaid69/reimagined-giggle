text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import re
def split_string(pattern, string):
        return re.split(pattern, string)