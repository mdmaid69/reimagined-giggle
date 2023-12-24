import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()