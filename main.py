numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)