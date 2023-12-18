  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare