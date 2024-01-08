  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()