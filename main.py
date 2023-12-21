text = "Hello, world!"
print("Reversed:", text[::-1])
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)