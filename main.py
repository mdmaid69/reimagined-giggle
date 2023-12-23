  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)