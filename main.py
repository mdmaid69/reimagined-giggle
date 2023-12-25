import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()