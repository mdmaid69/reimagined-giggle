  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()