n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)