  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()