import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
text = "Hello, world!"
print("Words:", len(text.split()))