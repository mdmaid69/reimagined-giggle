  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time