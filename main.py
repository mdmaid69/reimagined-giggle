  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)