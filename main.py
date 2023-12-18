  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()