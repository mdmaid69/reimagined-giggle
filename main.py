def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()