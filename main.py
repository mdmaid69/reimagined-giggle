  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()