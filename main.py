  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import os
def remove_directory(path):
        os.rmdir(path)