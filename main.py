  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)