  import os
  def get_base_name(path):
        return os.path.basename(path)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()