import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()