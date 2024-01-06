text = "Hello, world!"
print("Reversed:", text[::-1])
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)