text = "Hello, world!"
print("Characters:", len(text))
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)