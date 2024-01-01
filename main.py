import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
name = "Python"
print("Hello,", name)