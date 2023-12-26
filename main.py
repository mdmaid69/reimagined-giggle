import sklearn.datasets
print(sklearn.datasets.load_iris())
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()