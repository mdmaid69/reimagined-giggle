  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
def calculate_roi(gain, cost):
        return (gain - cost) / cost