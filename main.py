  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)