  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)