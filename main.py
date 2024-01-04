text = "Hello, world!"
print("Uppercase:", text.upper())
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)