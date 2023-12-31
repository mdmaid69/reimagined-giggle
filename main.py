sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)