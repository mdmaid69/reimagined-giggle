def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h