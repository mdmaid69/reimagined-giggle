import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))