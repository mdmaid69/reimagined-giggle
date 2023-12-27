  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time