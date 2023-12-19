  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import re
def split_string(pattern, string):
        return re.split(pattern, string)