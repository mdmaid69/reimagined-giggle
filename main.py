  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)