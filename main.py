import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def count_words(sentence):
        return len(sentence.split())