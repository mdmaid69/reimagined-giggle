numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)