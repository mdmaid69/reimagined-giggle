import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])