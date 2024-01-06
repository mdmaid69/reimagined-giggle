import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()