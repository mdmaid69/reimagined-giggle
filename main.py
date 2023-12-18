  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))