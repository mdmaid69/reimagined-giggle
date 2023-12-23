text = "Hello, world!"
print("Uppercase:", text.upper())
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)