import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()