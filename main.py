import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def sort_numbers(numbers):
        return sorted(numbers)