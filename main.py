import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)