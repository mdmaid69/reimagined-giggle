  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)