import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])