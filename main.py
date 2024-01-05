  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)