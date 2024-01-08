  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h