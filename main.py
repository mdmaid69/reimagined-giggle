def greet(name):
        print(f"Hello, {name}!")
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)