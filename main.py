  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)