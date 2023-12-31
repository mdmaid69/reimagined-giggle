n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)