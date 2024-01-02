  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)