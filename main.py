import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def sort_numbers(numbers):
        return sorted(numbers)