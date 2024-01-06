import collections
def create_counter():
        return collections.Counter()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))