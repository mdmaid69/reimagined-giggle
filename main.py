  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)