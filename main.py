  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread