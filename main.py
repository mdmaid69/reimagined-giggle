import re
def split_string(pattern, string):
        return re.split(pattern, string)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))