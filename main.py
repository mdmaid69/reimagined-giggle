sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)