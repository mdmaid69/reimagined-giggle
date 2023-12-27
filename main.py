import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()