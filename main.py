  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()