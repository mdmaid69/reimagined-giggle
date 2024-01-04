  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])