  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()