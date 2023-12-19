import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()