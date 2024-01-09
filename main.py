  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()