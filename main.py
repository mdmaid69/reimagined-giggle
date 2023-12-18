sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)