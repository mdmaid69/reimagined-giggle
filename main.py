  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns