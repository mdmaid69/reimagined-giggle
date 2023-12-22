import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)