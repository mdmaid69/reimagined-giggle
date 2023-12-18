  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import os
def get_environment_variable(var):
        return os.getenv(var)