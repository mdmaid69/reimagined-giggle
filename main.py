  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]