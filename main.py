import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()