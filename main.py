def calculate_roi(gain, cost):
        return (gain - cost) / cost
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()