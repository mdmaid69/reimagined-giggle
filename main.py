  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)