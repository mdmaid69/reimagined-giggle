x = 10
y = 20
print("Sum:", x + y)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h