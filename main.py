  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array