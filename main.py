import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])