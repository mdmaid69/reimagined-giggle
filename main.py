import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()