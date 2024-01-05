  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"