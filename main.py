  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)