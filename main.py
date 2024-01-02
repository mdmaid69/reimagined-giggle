  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()