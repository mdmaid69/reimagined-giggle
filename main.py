  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()