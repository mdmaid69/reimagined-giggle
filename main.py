  import os
  def get_base_name(path):
        return os.path.basename(path)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()