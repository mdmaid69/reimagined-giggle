  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import math
def calculate_combinations(n, k):
        return math.comb(n, k)