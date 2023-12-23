  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()