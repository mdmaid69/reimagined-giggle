  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)