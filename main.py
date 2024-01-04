  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()