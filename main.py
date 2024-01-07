  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)