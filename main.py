import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()