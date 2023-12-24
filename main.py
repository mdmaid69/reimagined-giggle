  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)