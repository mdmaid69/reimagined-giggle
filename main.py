  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)