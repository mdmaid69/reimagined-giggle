import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])