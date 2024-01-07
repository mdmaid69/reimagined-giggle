  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"