import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
text = "Hello, world!"
print("Reversed:", text[::-1])