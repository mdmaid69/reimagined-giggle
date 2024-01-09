  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
  import os
  def get_directory_name(path):
        return os.path.dirname(path)