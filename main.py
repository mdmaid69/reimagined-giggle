import datetime
print(datetime.datetime.now())
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)