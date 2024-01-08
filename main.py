import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def count_words(sentence):
        return len(sentence.split())