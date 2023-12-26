  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)