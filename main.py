import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()