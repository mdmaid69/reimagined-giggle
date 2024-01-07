import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def count_words(sentence):
        return len(sentence.split())