  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import os
def list_files_in_directory(path):
        return os.listdir(path)