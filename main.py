  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)