import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()