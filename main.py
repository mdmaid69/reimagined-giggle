sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))