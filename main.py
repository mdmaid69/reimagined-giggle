text = "Hello, world!"
print("Uppercase:", text.upper())
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)