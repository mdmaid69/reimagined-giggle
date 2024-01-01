  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)