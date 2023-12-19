import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()