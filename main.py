n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()