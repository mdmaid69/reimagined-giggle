  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()