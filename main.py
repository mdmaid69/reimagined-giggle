import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()