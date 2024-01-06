  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
def find_difference(list1, list2):
        return set(list1) - set(list2)