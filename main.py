import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()