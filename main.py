  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)