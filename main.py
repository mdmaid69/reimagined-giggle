  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)