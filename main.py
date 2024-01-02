numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)