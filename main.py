import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])