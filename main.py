  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import os
def list_files_in_directory(path):
        return os.listdir(path)