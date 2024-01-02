  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)