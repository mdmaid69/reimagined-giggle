import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()