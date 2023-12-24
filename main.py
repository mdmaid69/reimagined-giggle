  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()