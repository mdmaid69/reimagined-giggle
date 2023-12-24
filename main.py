  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import os
def change_working_directory(path):
        os.chdir(path)