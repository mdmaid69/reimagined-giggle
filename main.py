numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)