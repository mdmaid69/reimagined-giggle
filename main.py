  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()