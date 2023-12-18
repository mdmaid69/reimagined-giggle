  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)