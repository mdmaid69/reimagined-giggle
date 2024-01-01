  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)