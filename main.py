  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b