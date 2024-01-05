import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()