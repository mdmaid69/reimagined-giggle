import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()