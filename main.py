  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import math
def calculate_permutations(n, k):
        return math.perm(n, k)