import time
def get_time_since_epoch():
        return time.time()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()