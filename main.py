import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()