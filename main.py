  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
n = 10
print("Powers of 2:", [2**x for x in range(n)])