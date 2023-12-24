  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)