def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h