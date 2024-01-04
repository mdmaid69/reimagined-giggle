  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue