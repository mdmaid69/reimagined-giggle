import numpy as np
print(np.array([1, 2, 3]))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)