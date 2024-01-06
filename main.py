  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)