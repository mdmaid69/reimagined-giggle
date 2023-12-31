  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)