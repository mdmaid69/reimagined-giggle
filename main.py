  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)