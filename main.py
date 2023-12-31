  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def calculate_area_triangle(b, h):
        return 0.5 * b * h