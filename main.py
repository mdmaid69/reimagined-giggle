  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c