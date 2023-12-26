  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)