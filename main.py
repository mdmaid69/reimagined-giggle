  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time