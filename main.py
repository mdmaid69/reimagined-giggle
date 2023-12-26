  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)