import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))