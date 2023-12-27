import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)