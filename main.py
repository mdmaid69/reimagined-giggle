import collections
def count_elements(iterable):
        return collections.Counter(iterable)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))