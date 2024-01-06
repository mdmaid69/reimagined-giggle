sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)