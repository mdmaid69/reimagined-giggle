n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()