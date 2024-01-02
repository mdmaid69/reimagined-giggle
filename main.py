  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()