n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()