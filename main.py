import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def find_unique_words(sentence):
        return set(sentence.split())