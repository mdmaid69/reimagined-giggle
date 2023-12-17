def find_unique_words(sentence):
        return set(sentence.split())
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h