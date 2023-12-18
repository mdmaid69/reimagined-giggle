import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()