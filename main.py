text = "Hello, world!"
print("Words:", len(text.split()))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)