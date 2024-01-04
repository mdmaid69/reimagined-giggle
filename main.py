  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity