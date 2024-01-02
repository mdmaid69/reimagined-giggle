  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()