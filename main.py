  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()