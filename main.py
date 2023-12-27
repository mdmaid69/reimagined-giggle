n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h