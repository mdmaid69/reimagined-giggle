  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)