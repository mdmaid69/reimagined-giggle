  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)