  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)