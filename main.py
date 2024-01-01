def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)