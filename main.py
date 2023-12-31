text = "Hello, world!"
print("Uppercase:", text.upper())
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)