def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()