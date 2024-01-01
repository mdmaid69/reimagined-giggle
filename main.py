import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))