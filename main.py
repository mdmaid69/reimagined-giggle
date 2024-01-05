sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)