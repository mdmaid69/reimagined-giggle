  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)