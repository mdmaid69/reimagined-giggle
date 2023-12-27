import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()