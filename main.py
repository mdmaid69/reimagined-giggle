  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()