import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()