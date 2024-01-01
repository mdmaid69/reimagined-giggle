import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])