  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()