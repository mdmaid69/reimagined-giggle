import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()