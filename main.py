  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import re
def split_string(pattern, string):
        return re.split(pattern, string)