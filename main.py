import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()