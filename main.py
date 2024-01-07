import array
def get_array_itemsize(array):
        return array.itemsize
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()