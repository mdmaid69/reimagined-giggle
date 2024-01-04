  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)