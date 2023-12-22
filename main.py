import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
n = 10
print("Square numbers:", [x**2 for x in range(n)])