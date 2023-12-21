  import os
  def get_base_name(path):
        return os.path.basename(path)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()