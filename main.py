  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)