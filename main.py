  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()