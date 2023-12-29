  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)