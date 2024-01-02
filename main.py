  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")