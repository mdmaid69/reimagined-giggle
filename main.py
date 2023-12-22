import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))