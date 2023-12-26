  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)