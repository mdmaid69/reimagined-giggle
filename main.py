  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)