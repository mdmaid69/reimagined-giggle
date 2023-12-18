  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)