import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def is_odd(n):
        return n % 2 != 0