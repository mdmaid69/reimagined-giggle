  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink