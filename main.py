import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
text = "Hello, world!"
print("Words:", len(text.split()))