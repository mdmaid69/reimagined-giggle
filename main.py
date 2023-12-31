import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()