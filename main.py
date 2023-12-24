  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import os
  def get_current_working_directory():
        return os.getcwd()