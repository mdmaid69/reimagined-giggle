  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()