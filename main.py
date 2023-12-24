  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()