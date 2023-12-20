import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()