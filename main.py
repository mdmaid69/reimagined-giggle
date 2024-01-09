  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)