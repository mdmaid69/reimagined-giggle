  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)