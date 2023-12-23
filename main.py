import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h