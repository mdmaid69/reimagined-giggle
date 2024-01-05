import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)