import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()