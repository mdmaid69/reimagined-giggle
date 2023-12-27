  import os
  def split_path(path):
        return os.path.split(path)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()