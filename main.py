  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b