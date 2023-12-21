  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()