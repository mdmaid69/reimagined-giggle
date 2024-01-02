import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
n = 10
print("Powers of 2:", [2**x for x in range(n)])