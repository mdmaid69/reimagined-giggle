  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)