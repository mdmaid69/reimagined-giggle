import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()