text = "Hello, world!"
print("Uppercase:", text.upper())
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)