  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)