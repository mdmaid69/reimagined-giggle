  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)