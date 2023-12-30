import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()