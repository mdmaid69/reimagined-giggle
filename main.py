  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))