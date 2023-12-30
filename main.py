n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()