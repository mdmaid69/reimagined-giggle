  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)