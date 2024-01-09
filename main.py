import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
text = "Hello, world!"
print("Characters:", len(text))