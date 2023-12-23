  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius