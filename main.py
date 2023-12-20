  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)