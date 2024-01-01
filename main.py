numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)