  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()