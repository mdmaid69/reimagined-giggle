def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)