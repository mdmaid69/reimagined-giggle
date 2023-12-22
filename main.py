  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import array
def get_array_as_memoryview(array):
        return memoryview(array)