  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)