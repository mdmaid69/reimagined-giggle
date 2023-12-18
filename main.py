  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)