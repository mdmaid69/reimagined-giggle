  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
def find_union(list1, list2):
        return set(list1) | set(list2)