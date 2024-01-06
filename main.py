  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()