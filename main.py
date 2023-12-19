  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}