n = 10
print("Powers of 2:", [2**x for x in range(n)])
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()