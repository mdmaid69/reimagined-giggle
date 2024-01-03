text = "Hello, world!"
print("Words:", len(text.split()))
import re
def split_string(pattern, string):
        return re.split(pattern, string)