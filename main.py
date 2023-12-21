  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])