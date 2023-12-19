name = "Python"
print("Hello,", name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h