  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)