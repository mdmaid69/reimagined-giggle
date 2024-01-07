text = "Hello, world!"
print("Words:", len(text.split()))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)