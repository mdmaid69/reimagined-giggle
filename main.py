sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))