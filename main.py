  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)