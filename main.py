import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()