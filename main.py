import glob
def find_files(pattern):
        return glob.glob(pattern)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()