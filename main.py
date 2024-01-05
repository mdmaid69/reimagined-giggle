import array
def get_bytes_from_array(array):
        return array.tobytes()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()