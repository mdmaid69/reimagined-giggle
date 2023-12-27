import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])