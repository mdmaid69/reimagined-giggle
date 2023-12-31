sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)