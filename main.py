  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()