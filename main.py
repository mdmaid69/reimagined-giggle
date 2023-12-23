sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h