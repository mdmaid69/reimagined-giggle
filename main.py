  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)