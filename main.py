import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()