text = "Hello, world!"
print("Words:", len(text.split()))
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)