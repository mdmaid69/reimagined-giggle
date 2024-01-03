import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b