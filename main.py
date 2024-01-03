import glob
def find_files(pattern):
        return glob.glob(pattern)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()