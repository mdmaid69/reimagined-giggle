import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
n = 10
print("Powers of 2:", [2**x for x in range(n)])