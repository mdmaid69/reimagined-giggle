  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time