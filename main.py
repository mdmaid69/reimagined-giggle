numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h