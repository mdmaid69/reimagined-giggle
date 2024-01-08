  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))