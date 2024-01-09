  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)