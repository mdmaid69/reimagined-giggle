import re
print(re.match("h.*o", "hello world"))
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)