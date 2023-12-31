  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()