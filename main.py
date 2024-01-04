  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()