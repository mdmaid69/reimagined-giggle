import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()