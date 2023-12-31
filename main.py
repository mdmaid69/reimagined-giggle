import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()