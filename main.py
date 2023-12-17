  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)