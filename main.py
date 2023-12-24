  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import re
def split_string(pattern, string):
        return re.split(pattern, string)