import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
text = "Hello, world!"
print("Words:", len(text.split()))