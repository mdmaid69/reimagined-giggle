import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()