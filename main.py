  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)