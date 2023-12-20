  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()