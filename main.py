  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()