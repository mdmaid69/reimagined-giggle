  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"