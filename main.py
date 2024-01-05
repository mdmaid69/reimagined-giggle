def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)