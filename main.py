  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()