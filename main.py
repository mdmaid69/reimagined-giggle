  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()