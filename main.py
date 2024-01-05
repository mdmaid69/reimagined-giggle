import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()