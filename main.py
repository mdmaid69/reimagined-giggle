import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)