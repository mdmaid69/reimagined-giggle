import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
text = "Hello, world!"
print("Words:", len(text.split()))