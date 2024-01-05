  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)