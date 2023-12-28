  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)