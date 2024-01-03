numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()