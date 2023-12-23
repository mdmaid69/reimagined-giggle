  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)