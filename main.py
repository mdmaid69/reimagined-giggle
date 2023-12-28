  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps