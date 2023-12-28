  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()