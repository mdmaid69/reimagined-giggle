  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)