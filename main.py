  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b