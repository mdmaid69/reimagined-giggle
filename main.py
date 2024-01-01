import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])