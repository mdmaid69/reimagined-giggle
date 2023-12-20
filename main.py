import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()