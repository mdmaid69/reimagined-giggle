  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))