import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()