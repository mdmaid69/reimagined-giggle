  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)