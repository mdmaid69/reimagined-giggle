import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)