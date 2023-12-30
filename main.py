import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()