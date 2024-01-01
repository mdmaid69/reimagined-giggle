import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()