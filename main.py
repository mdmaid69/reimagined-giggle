  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h