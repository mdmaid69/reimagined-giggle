  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))