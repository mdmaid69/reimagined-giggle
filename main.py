  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import os
def list_files_in_directory(path):
        return os.listdir(path)