  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)