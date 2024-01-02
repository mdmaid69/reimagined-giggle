  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)