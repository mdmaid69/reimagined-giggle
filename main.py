  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h