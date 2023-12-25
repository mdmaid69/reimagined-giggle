  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import array
def convert_array_to_list(array):
        return array.tolist()