import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())