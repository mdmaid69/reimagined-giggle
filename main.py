import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()