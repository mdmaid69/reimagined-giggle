  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))