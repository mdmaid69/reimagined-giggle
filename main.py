  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}