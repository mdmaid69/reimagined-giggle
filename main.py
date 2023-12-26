import collections
def count_elements(iterable):
        return collections.Counter(iterable)
from collections import Counter
print(Counter("hello world"))