def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()