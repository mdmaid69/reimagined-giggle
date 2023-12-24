  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)