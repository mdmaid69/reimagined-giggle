  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)