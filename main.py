  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}