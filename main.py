  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()