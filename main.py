n = 10
print("Cube numbers:", [x**3 for x in range(n)])
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()