sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)