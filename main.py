  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()