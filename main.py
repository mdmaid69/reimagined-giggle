import math
def calculate_circle_area(radius):
        return math.pi * radius**2
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()