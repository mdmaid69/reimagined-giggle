  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)