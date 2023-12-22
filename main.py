  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()