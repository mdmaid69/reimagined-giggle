  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)