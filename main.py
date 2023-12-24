  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)