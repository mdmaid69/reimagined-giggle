  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b