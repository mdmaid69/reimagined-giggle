import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])