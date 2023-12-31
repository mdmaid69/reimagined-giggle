n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h