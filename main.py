import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)