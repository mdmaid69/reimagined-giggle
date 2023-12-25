import os
print(os.getcwd())
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)