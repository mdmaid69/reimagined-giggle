  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))