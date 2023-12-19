  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)