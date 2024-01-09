  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)