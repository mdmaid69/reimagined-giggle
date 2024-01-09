import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])