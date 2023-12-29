  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)