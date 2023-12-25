  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()