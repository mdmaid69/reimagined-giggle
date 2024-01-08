def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)