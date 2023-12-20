n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)