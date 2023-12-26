  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()