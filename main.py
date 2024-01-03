  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])