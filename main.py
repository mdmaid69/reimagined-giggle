  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets