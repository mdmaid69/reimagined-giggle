  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"