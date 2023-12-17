import glob
def find_files(pattern):
        return glob.glob(pattern)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()