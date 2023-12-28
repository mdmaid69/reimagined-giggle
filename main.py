  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"