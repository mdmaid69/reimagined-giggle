  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def find_union(list1, list2):
        return set(list1) | set(list2)