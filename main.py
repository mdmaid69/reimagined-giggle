import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def count_characters(sentence):
        return len(sentence)