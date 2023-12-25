import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()