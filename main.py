import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()