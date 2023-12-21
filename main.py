import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()