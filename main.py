  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)