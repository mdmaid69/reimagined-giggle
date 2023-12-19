  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)