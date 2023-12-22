  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)