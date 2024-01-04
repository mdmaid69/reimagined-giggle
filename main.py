  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)