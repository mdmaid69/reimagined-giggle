import numpy as np
print(np.array([1, 2, 3]))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)