sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)