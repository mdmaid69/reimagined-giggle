  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)