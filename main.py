def sort_numbers(numbers):
        return sorted(numbers)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h