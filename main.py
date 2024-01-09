import random
print(random.randint(0, 100))
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)