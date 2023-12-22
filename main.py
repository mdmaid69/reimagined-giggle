  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])