  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))