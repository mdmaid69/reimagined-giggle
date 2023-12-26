import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))