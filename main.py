import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()