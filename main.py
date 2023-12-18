def greet(name):
        print(f"Hello, {name}!")
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)