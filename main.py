text = "Hello, world!"
print("Words:", len(text.split()))
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)