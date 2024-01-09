  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()