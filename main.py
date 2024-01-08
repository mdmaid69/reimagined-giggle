import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
n = 10
print("Powers of 2:", [2**x for x in range(n)])