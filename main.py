text = "Hello, world!"
print("Uppercase:", text.upper())
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)