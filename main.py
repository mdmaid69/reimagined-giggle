  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)