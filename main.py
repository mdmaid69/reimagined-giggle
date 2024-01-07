n = 10
print("Square numbers:", [x**2 for x in range(n)])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h