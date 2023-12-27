import random
print(random.randint(0, 100))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h