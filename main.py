import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()