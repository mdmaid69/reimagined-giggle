  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)