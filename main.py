  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])