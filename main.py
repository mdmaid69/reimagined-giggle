  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()