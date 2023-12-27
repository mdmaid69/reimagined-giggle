  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps