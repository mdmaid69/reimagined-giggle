import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()