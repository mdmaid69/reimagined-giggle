def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)