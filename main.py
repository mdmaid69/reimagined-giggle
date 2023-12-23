  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()