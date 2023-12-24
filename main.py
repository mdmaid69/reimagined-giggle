import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))