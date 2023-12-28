def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)