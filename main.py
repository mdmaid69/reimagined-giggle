import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)