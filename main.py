  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height