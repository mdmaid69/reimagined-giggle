import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
n = 10
print("Square numbers:", [x**2 for x in range(n)])