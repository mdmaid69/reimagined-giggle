  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)