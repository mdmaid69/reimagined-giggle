  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)