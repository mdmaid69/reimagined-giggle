  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)