def find_unique_words(sentence):
        return set(sentence.split())
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)