def find_unique_words(sentence):
        return set(sentence.split())
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)