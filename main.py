import array
def get_string_from_array(array):
        return array.tobytes()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()