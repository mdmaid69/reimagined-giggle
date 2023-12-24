n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)