import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def count_words(sentence):
        return len(sentence.split())