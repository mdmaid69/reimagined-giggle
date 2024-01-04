  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)