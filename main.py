import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def greet(name):
        print(f"Hello, {name}!")