  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()