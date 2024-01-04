numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h