  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)