import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()