import glob
def find_files(pattern):
        return glob.glob(pattern)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()