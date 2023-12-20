import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])