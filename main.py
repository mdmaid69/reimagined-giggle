import itertools
print(list(itertools.permutations([1, 2, 3])))
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()