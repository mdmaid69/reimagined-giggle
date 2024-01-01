  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")