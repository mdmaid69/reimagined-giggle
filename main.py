n = 10
print("Powers of 2:", [2**x for x in range(n)])
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()