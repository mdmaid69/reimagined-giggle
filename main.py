i = 0
while i < 5:
        print(i)
        i += 1
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)