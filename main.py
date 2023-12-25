  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time