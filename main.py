import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()