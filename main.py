  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))