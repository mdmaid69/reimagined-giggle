  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)