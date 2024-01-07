import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])