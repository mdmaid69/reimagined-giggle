  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))