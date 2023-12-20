  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import os
def get_file_size(filename):
        return os.path.getsize(filename)