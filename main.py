def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)