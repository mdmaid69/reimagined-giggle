  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()