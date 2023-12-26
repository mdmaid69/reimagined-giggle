import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))