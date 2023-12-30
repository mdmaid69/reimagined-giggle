import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
n = 10
print("Square numbers:", [x**2 for x in range(n)])